class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def createLinkedList(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node

        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = node

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

def main():
    l1 = LinkedList()
    n = int(input("Enter the number of node you want to enter:"))
    for i in range(n):
        num = int(input(f"Enter the {i+1} node:"))
        l1.createLinkedList(num)
    l1.display()

if __name__ == "__main__":
    main()