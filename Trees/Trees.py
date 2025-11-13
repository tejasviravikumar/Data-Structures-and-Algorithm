class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def create_node(self,value):
        node = TreeNode(value)
        if not self.root:
            self.root = node

        Q = [self.root]
        while Q:
            curr = Q.pop(0)
            if not curr.left :
                curr.left = node
                return

            else:
                Q.append(curr.left)

            if not curr.right:
                curr.right = node
                return

            else:
                Q.append(curr.right)



def main():
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)

if __name__ == "__name__":
    main()