# Bottom-Up Recursion: MaxDepth Explained

##  The MaxDepth Code

```python
def MaxDepth(root):
    if not root:
        return 0

    return 1 + max(MaxDepth(root.left), MaxDepth(root.right))
```

##  KEY IDEA

**Bottom-up** = children are solved first → then the parent uses their results.  
This happens during the **return phase** of recursion.

**Top-down** = parent sends information downwards before children solve anything.

---

##  Let's See MaxDepth in Action on a Real Tree

```
        A
       / \
      B   C
     /
    D
```

---

##  Step-by-Step (Pay Attention to the Order)

### 1. Start at A → calls `MaxDepth(A.left)`
➡️ goes to **B**

### 2. From B → calls `MaxDepth(B.left)`
➡️ goes to **D**

### 3. From D → calls `MaxDepth(D.left)` and `MaxDepth(D.right)`
Both return `0`

Now we compute:
```python
MaxDepth(D) = 1 + max(0, 0) = 1
```

✔️ **Value for D is fully known. This is "bottom".**

### 4. Go back to B
Now B can compute:
```python
MaxDepth(B) = 1 + max(MaxDepth(D), MaxDepth(None))
            = 1 + max(1, 0)
            = 2
```

✔️ **Value for B is computed after children.**

### 5. Go back to A
Now A can compute:
```python
MaxDepth(A) = 1 + max(MaxDepth(B), MaxDepth(C))
```

`MaxDepth(C) = 1` (similar to D)

So:
```python
MaxDepth(A) = 1 + max(2, 1) = 3
```

---

##  This Was Bottom-Up Because…

✔️ You computed **D first**  
✔️ Then used **D to compute B**  
✔️ Used **B & C to compute A**  

❗ **Parent results depend entirely on children**  
❗ **The actual value is constructed during the return of recursion**  

✔️ **Recursion order: Left → Right → Node**  
= **Post-order** = **Bottom-up**

---

##  Visual Flow

```
Call Stack (Going Down):
A → B → D → None (return 0)
         ↓
    D calculates: 1
    ↓
B calculates: 2
↓
A calculates: 3

Bottom ➡️ Top
```

---

##  Key Takeaway

In bottom-up recursion:
- **Base cases** are hit first (the "bottom")
- Values bubble up through **returns**
- Each parent **waits** for children to finish
- The root gets its answer **last**