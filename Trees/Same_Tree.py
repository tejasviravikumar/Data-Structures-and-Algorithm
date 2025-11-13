class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def Same_Tree(p,q):
    if not p or not q: # First we are checking if the nodes exist or not  
        return p == q  # 

                            # (i)   P:None and Q:None
                            # (ii)  P:not None and Q:None
                            # (iii) P:None and Q: not None

    return p.val == q.val and Same_Tree(p.left,q.left) and Same_Tree(p.right,q.right) # if both nodes exists , we check the value and go call the other nodes recursively

def main():
    root1 = Tree(10)
    root1.left = Tree(20)
    root1.right = Tree(30)
    root1.left.left = Tree(40)
    root1.left.right = Tree(50)

    root2 = Tree(10)
    root2.left = Tree(20)
    root2.right = Tree(30)
    root2.left.left = Tree(40)
    root2.left.right = Tree(50)

    print(Same_Tree(root1,root2))

if __name__ == "__main__":
    main()















