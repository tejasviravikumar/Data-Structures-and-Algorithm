# Naive approach to solve : Balanced Tree Question

"""
Compute the height of the entire left subtree

Compute the height of the entire right subtree

Compare abs(leftHeight - rightHeight)

If the difference > 1 → unbalanced

Otherwise → recursively check the left and right children
"""
# Top Down approach :  we recompute the height again aand again so its ineffective
def height(node):   # It calculates the height of the tree
    if not node:
        return 0

    return 1 + max(height(node.left) , height(node.right))

def isBalanced(root):
    if not root:
        return True

    Lnode = height(root.left)
    Rnode = height(root.right)

    if abs(Lnode - Rnode) > 1:
        return False

    return isBalanced(root.left) and isBalance(root.right)

# This method is inefficient — O(n²) time — because height() is recomputed many times.

# The efficient solution is Bottom-Up early stopping guessing 1

def isBalanced(root):
    def height(node):
        if not node:
            return 0

        left = height(node.left)
        if node.left == -1:
            return -1

        right = height(node.right)
        if node.right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left,right)

    return height(root) != -1