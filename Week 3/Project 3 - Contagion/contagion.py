class Health:
    def __init__(self, susceptible, infected, recovery):
        self.susceptible = susceptible
        self.infected = infected
        self.recovery = recovery


class Person:
    def __init__(self, health, time_since_infection, distancing, mask):
        self.health = health
        self.time_s_r = time_since_infection
        self.distancing = distancing
        self.mask = mask

        