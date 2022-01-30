import enum
import random
import observer
import config
import math
from typing import List

import logging

# Set up logging (use as you did in Lab3 instead of debug print() statements)
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

    
class Health(enum.Enum):
    """Each individual is one discrete state of health, which we represent
    in this enumerated type (in Python there is no enum type, so we mimic it 
    with a class definition.)"""
    # enum.auto() simply returns an unused numerical value for this enumerated type
    # (e.g., 0, 1, 2, 3, ...) -- having more descriptive names for these values makes
    # the code easier to write and understand.
    SUSCEPTIBLE = enum.auto()    
    INFECTED = enum.auto()  
    RECOVERED = enum.auto()
    DEAD = enum.auto()
        
    @staticmethod
    def get_random() -> "Health":
        """Returns a random enumerated element"""
        return Health(random.randint(0, len(Health) - 1))

    def __str__(self) -> str:
        """Return a string representation of the health state"""
        return self.name.lower()


# ----------------------------------------------------------------

class Individual(observer.Observable):
    """A class to store all the data associated with a typical individual. The individual
    is observable so that other objects (e.g., the controller or view) can be notified
    when an individual changes state, e.g., becomes sick or recovers."""
    
    def __init__(self, location: tuple):
        """Initialize each individual with a location. By default, the health
        state is Health.SUSCEPTIBLE.
        
        Args:
            location: a tuple of the form (row, col)
        """
        super().__init__()
        self._state = Health.SUSCEPTIBLE
        self._next_state = Health.SUSCEPTIBLE
        self._row, self._col = location
        self._time_in_state = 0
        
        # Parameters
        self.config = config.DISEASE
     
    def __str__(self) -> str:
        """Returns the name of the individual, in this case the health state."""
        return self._state.name
    
    def set_health(self, health: Health):
        """Sets the health of the individual.
        
        Args:
            health: The health state to set. One of the five Health enumerated values:
                Health.SUSCEPTIBLE, Health.INFECTED, Health.RECOVERED, Health.DEAD
        """
        if health in list(Health):
            self._state = health

    def get_individual(self, x, y):
        return
            
    def get_health(self) -> Health:
        """Returns the health state of the individual."""
        return self._state
    
    def set_next_state(self, health: Health):
        """Sets the next state of the individual"""
        self._next_state = health
        
    def get_next_state(self) -> Health:
        """Returns the next health state of the individual"""
        return self._next_state
        
    def step(self, region: "Population"):
        """Next state"""
        # Basic state transitions are in common between all individuals
        if self.get_health() == Health.INFECTED:
            # We could die on any time step before we recover
            if self._time_in_state > self.config['T_Recover']:
                log.debug(f"Recovery at {self._row},{self._col}")
                self._next_state = Health.RECOVERED
            elif random.random() < self.config['P_Death']:
                log.debug(f"Death at {self._row},{self._col}")
                self._next_state = Health.DEAD

        # Social behavior differs among concrete classes so 
        # we put those rules in a separate method, which will
        # be implemented in subclasses of Individual
        self.social_interactions(region)
        
    def tick(self):
        """Time passes"""
        self._time_in_state += 1
        if self._state != self._next_state:
            self._state = self._next_state
            self.notify_all("newstate")
            # Reset clock
            self._time_in_state = 0
            
    def get_char(self) -> str:
        """Returns a single-character string for textual representations."""
        return self._state.name[0].upper()
    
    # TODO: Methods that you must implement are below, feel free to add more
    def social_interactions(self, region: "Population"):
        """Implements the updates dictated by the social interactions of
        the individual, using more of the self.config parameters.
        
        Args:
            region: the population of individuals to which this individual belongs
        """
        # TODO: This is where you should start implementing Parts 1 and 2 of the project
        neighbors = region.get_neighbors((self._row, self._col), max_dist=config.SOCIAL['Visit_Dist'])
        if config.SOCIAL['N_Visits'] >= 1:
            for i in range(math.floor(config.SOCIAL['N_Visits'])):
                neighbor = random.choice(neighbors)
                #neighbor = Individual(random.choice(region.get_neighbors((self._row, self._col), config.SOCIAL['Visit_Dist'])))
                person = region.get_individual(neighbor[0], neighbor[1])
                greet = self.hello(person)
                if greet:
                    self.meet(person)
        elif config.SOCIAL['N_Visits'] < 1:
            neighbor = random.choice(neighbors)
            person = region.get_individual(neighbor[0], neighbor[1])
            y_n = random.random()
            if y_n < config.SOCIAL['N_Visits']:
                # neighbor = Individual(random.choice(region.get_neighbors((self._row, self._col))))
                greet = self.hello(person)
                if greet is True:
                    self.meet(person)

    def hello(self, visitor: "Individual") -> bool:
        """True means 'welcome' and False means 'go away'"""
        y_n = random.random()
        if y_n <= config.SOCIAL['P_Greet']:
            return True
        else:
            return False

    def meet(self, other: "Individual"):
        """Two individuals meet.  Either may infect
        the other.
        """
        transmit = random.random()
        if self.get_health() == Health.INFECTED or other.get_health() == Health.INFECTED:
            if self.get_health() == Health.RECOVERED or other.get_health() == Health.RECOVERED:
                pass
            if transmit <= config.DISEASE['P_Transmit']:
                self.set_next_state(Health.INFECTED)
                other.set_next_state(Health.INFECTED)


# ----------------------------------------------------------------

class Population(observer.Observable):
    """A model for the population based on a grid of cells, where each cell can hold
    a single Individual object. The population is observable, so that the view can
    get notified of changes to the population and update its visualization.
    
    """
    def __init__(self, num_rows: int, num_cols: int, num_people: int):
        """Initialize the population with a grid of nrows x ncols cells and
        randomly located npeople individuals, who are all intialized as vulnerable.
        
        Args:
            num_rows: The number of rows in the grid.
            num_cols: The number of columns in the grid.
            num_people: The initial number of people in the population.
        """
        super().__init__()
        
        self._step_num = 0
        self._nrows = num_rows
        self._ncols = num_cols
        self._people = []
        self._grid = [[None for i in range(num_rows)] for j in range(num_cols)]
        
        # TODO: add npeople Individuals to the population in random cells
        cells = []  # list of cells represented by (row, col) index tuples
        while len(cells) < min(num_people, num_rows * num_cols):
            i = random.randint(0, num_rows - 1)
            j = random.randint(0, num_cols - 1)
            if not (i, j) in cells: 
                cells.append((i,j))
        
        for row, col in cells:
            person = Individual(location=(row, col))
            self._people.append(person)
            self._grid[row][col] = person
        
    def __str__(self) -> str:
        """Returns a string representation of the population"""
        res = ''
        for i in range(self._nrows):
            for j in range(self._ncols):
                if self._grid[i][j] is None:
                    res += '.'.center(3)
                else:
                    # self._grid[i][j] is an Individual
                    res += self._grid[i][j].get_char().center(3)
            res += '\n'
        return res    
    
    def get_individual(self, row: int, col: int):
        """Return the individual at the specified row and column, or None"""
        if row < 0 or row > self._nrows or col > self._ncols or col < 0:
            raise ValueError("Invalid row or column")
        return self._grid[row][col]
        
    def step(self): 
        """Perform a single update the entire population grid.
        This iterates over the grid elements and invokes their step() method.
        """
        for row in range(self._nrows):
            for col in range(self._ncols):
                if self._grid[row][col] is not None:
                    self._grid[row][col].step(region=self)

        self.notify_all("Grid updated")    
    
    def tick(self):
        """Advance the time step for the whole grid."""
        self._step_num += 1
    
        for row in range(self._nrows):
            for col in range(self._ncols):
                if self._grid[row][col] is not None:
                    self._grid[row][col].tick()
                    
        self.notify_all("Grid updated")

    def seed(self, num_sick: int = config.POPULATION['N_Infected']):
        """Select a random subset of the individuals and make them sick.
        We only do this once, in the beginning of the simulation.
        
        Args:
            num_sick: The number of sick individuals to select.
        """
        infected_list = random.sample(self._people, num_sick)
        for person in infected_list:
            person.set_health(Health.INFECTED)
            person.set_next_state(Health.INFECTED)  # stay infected in next step
                
    def get_neighbors(self, coord: tuple, max_dist: int = 1) -> List[tuple]:
        """Returns a list of neighboring individual closer than the max distance.
        
        Args:
            coord: The tuple of (row, col) coordinates of the individual.
            max_dist: The maximum distance of the neighbors to collect
            
        Returns:
            A list of coordinate tuples (row, col) of neighbors within 
            within max_dist of the given coordinate.
        """
        # TODO: Implement for Part 1 with the default max_dist = 1, then extend for Part 2
        # to handle any distance within the grid. Do NOT return None values
        neighbors = []
        result = []
        # if max_dist == 1:
        #     neighbors.extend([(coord[0] - 1, coord[1] - 1), (coord[0] - 1, coord[1]), (coord[0] - 1, coord[1] + 1),
        #                   (coord[0], coord[1] - 1),                             (coord[0], coord[1] + 1),
        #                   (coord[0] + 1, coord[1] - 1), (coord[0] + 1, coord[1]), (coord[0] + 1, coord[1] + 1)])
        # elif max_dist == 2:
        #     neighbors.extend([(coord[0] - 2, coord[1] - 2), (coord[0] - 2, coord[1] - 1), (coord[0] - 2, coord[1] - 0),
        #                       (coord[0] - 2, coord[1] + 1), (coord[0] - 2, coord[1] + 2),
        #                       (coord[0] - 1, coord[1] - 2), (coord[0] - 1, coord[1] - 1), (coord[0] - 1, coord[1] - 0),
        #                       (coord[0] - 1, coord[1] + 1), (coord[0] - 2, coord[1] + 2),
        #                       (coord[0] - 0, coord[1] - 2), (coord[0] - 0, coord[1] - 1),
        #                       (coord[0] - 0, coord[1] + 1), (coord[0] - 2, coord[1] + 2),
        #                       (coord[0] + 1, coord[1] - 2), (coord[0] + 1, coord[1] - 1), (coord[0] + 1, coord[1] - 0),
        #                       (coord[0] + 1, coord[1] + 1), (coord[0] + 1, coord[1] + 2),
        #                       (coord[0] + 2, coord[1] - 2), (coord[0] + 2, coord[1] - 1), (coord[0] + 2, coord[1] - 0),
        #                       (coord[0] + 2, coord[1] + 2), (coord[0] + 2, coord[1] + 2)])

        # for i in self._grid:
        #     if math.sqrt(((i.coord[0] - coord[0]) ** 2) + (i.coord[1] - coord[1] ** 2)) < max_dist:
        #         neighbors.append(i)
        for i in range(self._nrows):
            for e in range(self._ncols):
                if math.sqrt((i - coord[0]) ** 2 + (e - coord[1]) ** 2) <= max_dist:
                    neighbors.append((i, e))


                for z in neighbors:
                    if z[0] < 0 or z[0] > self._ncols - 1 or z[1] < 0 or z[1] > self._nrows - 1:
                        pass
                    else:
                        result.append(z)
        return result

