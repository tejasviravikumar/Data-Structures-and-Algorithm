class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def Helper(Lnode , Rnode):
    if not Lnode and not Rnode:
        return Lnode == Rnode

    return Lnode.val == Rnode.val and Helper(Lnode.left,Rnode.right) and Helper(Lnode.right,Rnode.left)

def Symmetry(root):
    return Helper(root.left,root.right)


def main():
    root1 = Tree(10)
    root1.left = Tree(20)
    root1.right = Tree(20)
    root1.left.left = Tree(30)
    root1.left.right = Tree(40)
    root1.right.left = Tree(40)
    root1.right.right = Tree(30)

    root2 = Tree(10)
    root2.left = Tree(20)
    root2.right = Tree(20)
    root2.left.left = Tree(30)
    root2.left.right = Tree(40)
    root2.right.left = Tree(70)
    root2.right.right = Tree(40)

    print(f"Tree 1:{Symmetry(root1)}")
    print(f"Tree 2:{Symmetry(root2)}")
if __name__ == "__main__":
    main()