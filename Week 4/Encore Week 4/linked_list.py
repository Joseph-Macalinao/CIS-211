class Node:
    """
    Holds a piece of data and points to another node
    object
    """
    def __init__(self, data=None) -> None:
        self.data = data  # data to store 
        self.next = None  # another node

class LinkedList:
    """
    """
    def __init__(self):
        """
        the head will be the first element in the linked
        list
        """
        self.head = None  # a node

    def __search(self, item):
        """
        Search for data in linked list

        If found, return node that holds the found data.
        If data not found in list, return False
        """
        item.strip()
        current = self.head
        while current:
            if current.data == item:
                return current
            current = current.next
        return False
         
    def printList(self):
        """
        Prints List from head to tail

        for example: if LList has elements {1,2,3},
        where head holds data 1 and tail holds 3,
        then print "Head -> 1 -> 2 -> 3 -> None"
        """
        current = self.head
        string = "Head -> "
        # TODO - COMPLETE METHOD
        print(string + "None")

    def edit(self, current_data, new_data):
        """
        Edit data in list.

        If current data exists in list, replace it with
        new data. If current data does not exist in the list,
        print some message indicating failure
        """
        node = self.__search(current_data)
        if node:
            node.data = new_data
            print(f"{current_data} replaced by {new_data}")
        else:
            print(f"{current_data} not replaced because it is not in list")
         
    def push(self, data):
        """
        add new element at head of linked list

        (new element replaces old element)

        for example, assume LL is a LinkedList() with elements {1,2,3} 
        and you want to add 4. The new head must be 4 and the list 
        will be {4, 1, 2, 3}
        """
        # TODO - IMPLEMENT ME!