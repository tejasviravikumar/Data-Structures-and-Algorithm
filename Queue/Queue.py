class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def Append(self, value):
        if len(self.queue) < self.size:
            self.queue.append(value)
        else:
            print("Overflow! Queue is full.")

    def Insert(self, value, position):
        if len(self.queue) < self.size:
            if 0 <= position <= len(self.queue):
                self.queue.insert(position, value)
            else:
                print("Invalid position.")
        else:
            print("Overflow! Queue is full.")

    def Delete(self):
        if len(self.queue) == 0:
            print("Underflow! Queue is empty.")
        else:
            removed = self.queue.pop(0)
            print(f"Deleted element: {removed}")

    def Display(self):
        print(f"Queue: {self.queue}")

    def PeekFront(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print(f"Front element (top): {self.queue[0]}")

    def PeekRear(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print(f"Rear element: {self.queue[-1]}")


def main():
    size = int(input("Enter the size of the queue: "))
    q1 = Queue(size)

    while True:
        print("\nOPERATIONS ---")
        print("1. Append (enqueue)")
        print("2. Delete (dequeue)")
        print("3. Display queue")
        print("4. Peek Front (top)")
        print("5. Peek Rear")
        print("6. Exit")

        n = int(input("Enter your choice (1-6): "))
        match n:
            case 1:
                num = int(input("Enter a number to append: "))
                q1.Append(num)
            case 2:
                q1.Delete()
            case 3:
                q1.Display()
            case 4:
                q1.PeekFront()
            case 5:
                q1.PeekRear()
            case 6:
                print("Exiting...")
                break
            case _:
                print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
