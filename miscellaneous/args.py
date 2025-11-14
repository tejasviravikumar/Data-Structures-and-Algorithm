def groceries(*args):
    print(args)
    total = sum(args)
    return f"Total price: ₹{total}"

print(groceries(10, 20, 30))


def groceries(*args):
    total = sum(args)
    return f"Total price: ₹{total}"

prices = [10, 20, 30]

# 👇 Unpacking the list into individual arguments
print(groceries(*prices))
