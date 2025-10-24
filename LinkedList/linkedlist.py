class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, "->", end=" ")
            temp = temp.next
        print("None")

    def insert_front(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

# 1 2 3 4 
    
    def insert_at(self,value,pos):
        new_node = Node(value)
        temp = self.head

        if not temp or pos == 0:
            new_node.next = self.head
            self.head = new_node
            return 

        else:
            count = 0
            while pos - 1 > count and temp is not None :
                temp = temp.next
                count += 1

            if temp is None:
                print("Position out of bounds")
            new_node.next = temp.next
            temp.next = new_node

    def delete(self,value):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        if temp.value == value:
            self.head = temp.next
            return

        prev = None
        while temp.value != value:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Value not found")
            return 

        prev.next = temp.next

    def delete_duplicate(self , value):
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy
        
        while curr.next != None:
            if curr.next.value == value:
                curr.next = curr.next.next
            
            else:
                curr = curr.next

        self.head = dummy.next
        
        
def main():
    ll = LinkedList()
    n = int(input("Enter the number of elements: "))
    for _ in range(n):
        element = int(input("Enter element: "))
        ll.append(element)

    print("\nLinked List:")
    ll.display()
    ll.delete_duplicate(7)
    ll.display()
if __name__ == "__main__":
    main()
