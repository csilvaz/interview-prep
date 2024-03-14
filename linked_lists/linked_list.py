## Linked List Implementation

## Node Class:
## - Data
## - Reference to next node
class Node:
    def __init__(self, data) -> None: ## Type hint is 'None'
        self.data = data
        self.next = None


## LinkedList Class
## - Head: Reference to first node
## - Method: Insert at beginning
## - Method: Print to python list
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    ## Insertion (at beginning)
    ## Constant time operation O(1)
    def insert_at_beginning(self, data):
        # Create new node
        new_node = Node(data)

        # Check if head is already pointing to a node
        if self.head is None: #i.e. if head is not pointing to anything
            # Just point head to the new node
            self.head = new_node
            return
        else: # Otherwise...head IS pointing to another node
            ## 1. Point our new_node to the current first node
            new_node.next = self.head
            ## 2. Point the head to the new node
            self.head = new_node


    def to_list(self):
        elements = [] ## Create an empty python list (AKA dynamic array)
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def find(self, target):
        curr = self.head
        while curr:
            if target == curr.data: ## found the value
                return curr
            curr = curr.next
        return None 

