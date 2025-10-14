class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def createLinkedList(self,value):
        """Add a new node with given value at the end of the linked list."""
        node = Node(value)
        if self.head is None:
            self.head = node

        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = node

    def display(self):
        """Print all elements of the linked list."""
        curr = self.head

        if curr is None:
            print("Linked list is empty")

        else:
            while curr is not None:
                print(curr.value)
                curr = curr.next

def main():
    l1 = LinkedList()
    n = int(input("Enter the number of nodes you want to enter:"))
    for i in range(n):
        num = int(input(f"Enter node {i+1}:"))
        l1.createLinkedList(num)
    print("Linked List Elements :")
    l1.display()

if __name__ == "__main__":
    main()