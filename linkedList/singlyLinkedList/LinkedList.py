from Node import Node

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse(self):
        if self.start_node is None:
            return "LinkedList is empty"
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
