#Diego Espinola
#02.25.2020
# link list.

class Node:
    def __init__(self,data):
        self.data = None
#add to the head
class Linked_list:
    def __init__(self,data):
        self.head = None

    def add_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head=new_node
#add to the end
    def add_to_the_end (self,data):
        new_node=Node(data)
        current=self.head
        while current.next:
            current = current.next
        current.next = new_node
#remove from the head:
    def remove_head(self):
        new_node= self.head
        self.head= self.head.next
        return new_node.data

#remove to the end:
    def remove_end(self):
        current_node=self.head
        previous_node=self.head
        while current_node.next:
            previous_node= current_node
            current_node= current_node.next
        previous_node.next = None
        return previous_node.data






