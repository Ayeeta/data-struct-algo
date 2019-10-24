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
        print(total)

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            
            elems.append(cur_node.data)
        print(elems)
        


singly_1 = Linked_List()

singly_1.add_item(2)
singly_1.add_item(4)
singly_1.add_item(3)
singly_1.length()

