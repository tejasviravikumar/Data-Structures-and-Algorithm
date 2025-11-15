# There are Two ways you can find the height if the tree 
# (i) Using a helper function
# (ii) Without using a helper functiom

# Using Helper function : height()
def height(node):
    if not node:
        return 0

    return 1 + max(height(node.left) , height(node.right))

def MaxDepth(root):
    if not root:
        return 0

    return height(root)

# Not using a helper function

def MaxDepth(root):
    if not root:
        return 0

    return 1 + max(MaxDepth(root.left) , MaxDepth(root.right))