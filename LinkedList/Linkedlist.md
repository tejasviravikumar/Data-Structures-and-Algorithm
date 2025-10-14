# Linked List Implementation - Beginner's Guide

## What is This Program?
This is a simple Python program that creates a **linked list** - a way to store a collection of numbers where each number knows where to find the next number.

## What is a Linked List?
Imagine a chain where each link is connected to the next one:

```
[10] → [20] → [30] → [40] → END
```

- Each box contains a number (we call this a "node")
- Each node points to the next node with an arrow
- The last node points to nothing (the end)

**Why use a linked list instead of a regular list?**
- Easy to add items without moving everything around
- Good for learning how data structures work
- Foundation for understanding more complex topics

## What Does This Program Do?

1. Asks you how many numbers you want to store
2. Lets you enter each number one by one
3. Creates a linked list with all your numbers
4. Shows you all the numbers in order

## Understanding the Code

### Part 1: The Node Class
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

**What it does:**
- A `Node` is like one box in our chain
- `value` is the number stored in the box
- `next` is the arrow pointing to the next box (starts as `None` meaning "nothing yet")

**Example:** If you create a node with value 10:
- `value = 10`
- `next = None` (not connected to anything yet)

### Part 2: The LinkedList Class
```python
class LinkedList:
    def __init__(self):
        self.head = None
```

**What it does:**
- `LinkedList` manages the entire chain
- `head` is the first node in the chain (like the start of the treasure hunt)
- When we create a new list, it's empty, so `head = None`

### Part 3: Adding Nodes (createLinkedList method)
```python
def createLinkedList(self, value):
    node = Node(value)
    if self.head is None:
        self.head = node
    else:
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
```

**What it does:**
1. Creates a new node with your number
2. If the list is empty (no head), make this node the head
3. If the list has items, walk to the end of the chain
4. Connect the last node to the new node

**Visual Example:**

Starting with empty list, adding 10:
```
head → [10|None]
```

Adding 20:
```
head → [10] → [20|None]
```

Adding 30:
```
head → [10] → [20] → [30|None]
```

### Part 4: Displaying the List (display method)
```python
def display(self):
    curr = self.head
    if curr is None:
        print("Linked list is empty")
    else:
        while curr is not None:
            print(curr.value)
            curr = curr.next
```

**What it does:**
1. Start at the head (first node)
2. If empty, print a message
3. Otherwise, print the current node's value
4. Move to the next node
5. Repeat until you reach the end (`None`)

**Like reading the chain:** Start at the beginning and follow the arrows until you reach the end!

### Part 5: Main Program
```python
def main():
    l1 = LinkedList()
    n = int(input("Enter the number of nodes you want to enter:"))
    for i in range(n):
        num = int(input(f"Enter node {i+1}:"))
        l1.createLinkedList(num)
    print("Linked List Elements :")
    l1.display()
```

**What it does:**
1. Creates an empty linked list
2. Asks how many numbers you want
3. Uses a loop to get each number from you
4. Adds each number to the list
5. Shows all the numbers

## How to Run This Program

### Step 1: Save the Code
Copy the code into a file called `linked_list.py`

### Step 2: Open Terminal/Command Prompt
- **Windows:** Press `Win + R`, type `cmd`, press Enter
- **Mac:** Press `Cmd + Space`, type `terminal`, press Enter
- **Linux:** Press `Ctrl + Alt + T`

### Step 3: Navigate to Your File
```bash
cd path/to/your/file
```

### Step 4: Run the Program
```bash
python linked_list.py
```

## Example Run

```
Enter the number of nodes you want to enter: 4
Enter node 1: 5
Enter node 2: 10
Enter node 3: 15
Enter node 4: 20
Linked List Elements :
5
10
15
20
```

**What happened:**
- You told it you want 4 numbers
- You entered: 5, 10, 15, 20
- The program created: [5] → [10] → [15] → [20]
- Then it printed each number

## Common Mistakes to Avoid

1. **Forgetting to install Python:** Make sure Python is installed on your computer
2. **Typos in the code:** Copy the code carefully
3. **Entering letters instead of numbers:** The program expects numbers only
4. **Not saving the file:** Save with `.py` extension

## Practice Exercises

Try these to learn more:

1. **Modify the program** to ask for your name along with numbers
2. **Count the nodes:** Add a function that tells you how many nodes are in the list
3. **Find the largest number:** Add a function to find the biggest value
4. **Add at the beginning:** Modify `createLinkedList` to add nodes at the start instead of the end

## Key Terms Explained

- **Node:** One element in the linked list (contains data and a pointer)
- **Head:** The first node in the list
- **Next:** The pointer/reference to the next node
- **None:** Python's way of saying "nothing" or "empty"
- **Traverse:** Walking through the list from start to end

## Next Steps

Once you understand this program, try learning:
- Deleting nodes from a linked list
- Searching for a specific value
- Reversing a linked list
- Doubly linked lists

Happy coding! 🚀