class Arrays:
    def __init__(self,size):
        self.size = size
        self.arr = []
    
    def Append(self,value):
        if len(self.arr) < self.size:
            self.arr.append(value)

        else:
            print("Overflow! Cannot append.")
        
    def Insert(self,position,value):
        if len(self.arr) >= self.size:
            print("Overflow! Cannot insert.")
        elif position < 0 or position > len(self.arr):
            print("Invalid position!")
        else:
            self.arr.insert(position, value)

    def Delete(self,value):
        if len(self.arr) == 0:
            print("Underflow! Array is empty.")
        elif value in self.arr:
            self.arr.remove(value)
            print(f"{value} deleted.")
        else:
            print("Value not found!")

    def Display(self):
        print("Current Array:", self.arr)

def main():
    size = int(input("Enter the size of the array:"))
    arr1 = Arrays(size)
    while True:
        print("1.Append an element")
        print("2.Insert an element in a specific position")
        print("3.Delete an element")
        print("4. Display array")
        print("5. Exit")
        n = int(input("Enter a number to perform an operation (1-5):"))
        match n:
            case 1:
                num = int(input("Enter a number to append:"))
                arr1.Append(num)

            case 2:
                num = int(input("Enter a number to insert:"))
                pos = int(input("Enter the position to insert the value:"))
                arr1.Insert(pos,num)
            
            case 3:
                num = int(input("Enter a number to delete:"))
                arr1.Delete(num)

            case 4:
                arr1.Display()

            case 5:
                print("Exiting...")
                break

            case _:
                print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

            




