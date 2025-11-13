class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node

        else:
            t