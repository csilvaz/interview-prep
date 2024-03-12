class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # O(1): Constant time
    def insert_at_beginning(self, data):
        # Create Node
        new_node = Node(data)

        # Is the head an empty node?
        if self.head is None:
            # If so, then have the head point to the new node
            self.head = new_node
            return
        else: # If head is already pointing to another node
            new_node.next = self.head   # point the new node to the head pointer (i.e. the current head)
            self.head = new_node        # point the head to the new node