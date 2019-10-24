class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = Node()
    
    def add_item(self, data):
        new_node = Node(data)
        current_node = self.head
        
        while current_node.next != None:
            current_node = current_node.next
        current_node = new_node

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total

    def display(self):
        linked_list = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            linked_list.append(current_node.data)
        print(linked_list)


singly_1 = Linked_List()
singly_1.add_item(2)