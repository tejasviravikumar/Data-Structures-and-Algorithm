# Array Class Implementation - Detailed Explanation

## Table of Contents
1. [Overview](#overview)
2. [Class: Arrays](#class-arrays)
   - [Constructor: `__init__(self, size)`](#constructor-__init__self-size)
3. [Methods](#methods)
   - [1. `Append(self, value)`](#1-appendself-value)
   - [2. `Insert(self, position, value)`](#2-insertself-position-value)
   - [3. `Delete(self, value)`](#3-deleteself-value)
   - [4. `Display(self)`](#4-displayself)
4. [Main Program Flow](#main-program-flow)
   - [Menu Options](#menu-options)
5. [Key Concepts Demonstrated](#key-concepts-demonstrated)
   - [1. Fixed-Size Array](#1-fixed-size-array)
   - [2. Overflow and Underflow Handling](#2-overflow-and-underflow-handling)
   - [3. Error Validation](#3-error-validation)
   - [4. Match-Case Statement](#4-match-case-statement)
6. [Example Usage Session](#example-usage-session)
7. [Time Complexity](#time-complexity)

---

## Overview
This Python program implements a custom **fixed-size array** data structure with basic operations like append, insert, delete, and display. Unlike Python's built-in lists which can grow indefinitely, this class enforces a maximum size limit.

---

## Class: `Arrays`

### Constructor: `__init__(self, size)`
```python
def __init__(self, size):
    self.size = size
    self.arr = []
```

**Purpose:** Initializes a new array with a fixed maximum capacity.

**Parameters:**
- `size`: The maximum number of elements the array can hold

**Attributes:**
- `self.size`: Stores the maximum capacity
- `self.arr`: An empty Python list that will store the actual elements

**Example:**
```python
arr1 = Arrays(5)  # Creates an array with max capacity of 5
```

---

## Methods

### 1. `Append(self, value)`
```python
def Append(self, value):
    if len(self.arr) < self.size:
        self.arr.append(value)
    else:
        print("Overflow! Cannot append.")
```

**Purpose:** Adds an element to the end of the array.

**Logic:**
- Checks if there's space available (`current length < max size`)
- If yes: adds the value to the end
- If no: displays an "Overflow" error message

**Example:**
```python
arr1.Append(10)  # Adds 10 to the array
arr1.Append(20)  # Adds 20 to the array
```

---

### 2. `Insert(self, position, value)`
```python
def Insert(self, position, value):
    if len(self.arr) >= self.size:
        print("Overflow! Cannot insert.")
    elif position < 0 or position > len(self.arr):
        print("Invalid position!")
    else:
        self.arr.insert(position, value)
```

**Purpose:** Inserts an element at a specific position in the array.

**Parameters:**
- `position`: The index where the value should be inserted (0-based indexing)
- `value`: The element to insert

**Validation Checks:**
1. **Overflow check:** Ensures array isn't already full
2. **Position validation:** Ensures position is valid (between 0 and current length)
3. If both pass, inserts the value at the specified position

**Example:**
```python
arr1.Insert(0, 5)   # Inserts 5 at index 0 (beginning)
arr1.Insert(2, 15)  # Inserts 15 at index 2
```

---

### 3. `Delete(self, value)`
```python
def Delete(self, value):
    if len(self.arr) == 0:
        print("Underflow! Array is empty.")
    elif value in self.arr:
        self.arr.remove(value)
        print(f"{value} deleted.")
    else:
        print("Value not found!")
```

**Purpose:** Removes the first occurrence of a specific value from the array.

**Logic:**
1. **Underflow check:** Ensures array isn't empty
2. **Value search:** Checks if the value exists in the array
3. If found: removes it and confirms deletion
4. If not found: displays error message

**Example:**
```python
arr1.Delete(10)  # Removes the value 10 from the array
```

---

### 4. `Display(self)`
```python
def Display(self):
    print("Current Array:", self.arr)
```

**Purpose:** Prints the current contents of the array.

**Example Output:**
```
Current Array: [5, 10, 15, 20]
```

---

## Main Program Flow

The `main()` function provides an interactive menu-driven interface:

1. **Initialize:** Prompts user to enter the array size
2. **Menu Loop:** Continuously displays options until user exits
3. **Operations:** Uses `match-case` (Python 3.10+) for clean operation selection

### Menu Options:
1. **Append** - Add element to the end
2. **Insert** - Add element at specific position
3. **Delete** - Remove a specific value
4. **Display** - Show current array contents
5. **Exit** - Terminate the program

---

## Key Concepts Demonstrated

### 1. **Fixed-Size Array**
Unlike Python's dynamic lists, this implementation enforces a maximum capacity, similar to arrays in languages like C or Java.

### 2. **Overflow and Underflow Handling**
- **Overflow:** Attempting to add elements when the array is full
- **Underflow:** Attempting to delete from an empty array

### 3. **Error Validation**
The class includes proper error checking for:
- Array capacity limits
- Invalid positions
- Missing values
- Empty array operations

### 4. **Match-Case Statement**
Uses Python 3.10+ pattern matching for cleaner menu selection logic.

---

## Example Usage Session

```python
Enter the size of the array: 3

1. Append an element
Enter a number to append: 10
# Array: [10]

1. Append an element
Enter a number to append: 20
# Array: [10, 20]

2. Insert an element in a specific position
Enter a number to insert: 15
Enter the position to insert the value: 1
# Array: [10, 15, 20]

1. Append an element
Enter a number to append: 30
# Output: Overflow! Cannot append.

3. Delete an element
Enter a number to delete: 15
# Output: 15 deleted.
# Array: [10, 20]
```

---

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Append    | O(1)          |
| Insert    | O(n)          |
| Delete    | O(n)          |
| Display   | O(n)          |

**Note:** Insert and Delete are O(n) because they may require shifting elements.