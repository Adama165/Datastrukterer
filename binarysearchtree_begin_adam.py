class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class. 
    class Node:
        __slots__ = 'val', 'left', 'right'
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
            
        def getVal(self):
            return self.val
        
        def setVal(self,newval):
            self.val = newval
            
        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right
        
        def setLeft(self,newleft):
            self.left = newleft
            
        def setRight(self,newright):
            self.right = newright
            
        # This method deserves a little explanation. It does an inorder traversal
        # of the nodes of the tree yielding all the values. In this way, we get
        # the values in ascending order.
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
                    
            yield self.val
            
            if self.right != None:
                for elem in self.right:
                    yield elem

        def __repr__(self):
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
            
    # Below are the methods of the BinarySearchTree class. 
    def __init__(self, root=None):
        self.root = root
        
    def insert(self,val):
        self.root = BinarySearchTree.__insert(self.root,val)
        
    def __insert(root,val):
        if root == None:
            return BinarySearchTree.Node(val)
        
        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(),val))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(),val))
            
        return root
        
    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"

    def min(self):
        # TODO: Implement min, that uses the recursive __min
        if self.root is None:
            return None
        return BinarySearchTree.__min(self.root)
    
    def __min(root):
        # TODO: Implement the recursive __min, that returns the minimum of a subtree with the given root
        if root.left is None:
            return root.val
        return BinarySearchTree.__min(root.left)

    def max(self):
        # TODO: Implement max, that uses the recursive __max
        if self.root is None:
            return None
        return BinarySearchTree.__max(self.root)

    def __max(root):
        # TODO: Implement the recursive __max, that returns the maximum of a subtree with the given root
        if root.right is None:
            return root.val
        return BinarySearchTree.__max(root.right)

    def remove(self, val):
        # TODO: Implement remove, that uses the recursive __remove
        self.root = BinarySearchTree.__remove(self.root, val)
        return self.root
    
    def __remove(root, val):
        # TODO: Implement the recursive __remove that deletes val from the subtree with the given root
        # __remove returns the new subtree
        if root is None:
            return root
        if val == root.getVal():
            if root.getLeft() == None:
                return root.getRight()
            if root.getRight() == None:
                return root.getLeft()
            replaceVal = BinarySearchTree.__min(root.getRight())
            root.setVal(replaceVal)
            newSubTree = BinarySearchTree.__remove(root.getRight(),replaceVal)
            root.setRight(newSubTree)
            return root
        
        if val > root.getVal():
            newSubTree = BinarySearchTree.__remove(root.getRight(),val)
            root.setRight(newSubTree)

        else:
            newSubTree = BinarySearchTree.__remove(root.getLeft(),val)
            root.setLeft(newSubTree)

        return root

    def __contains__(self, val):
        # TODO: Implement __contains__, that uses the recursive __contains
        # Return True if val is in the tree, and False otherwise
        return BinarySearchTree.__contains(self.root, val)

    def __contains(root, val):
        # TODO: Implement the recursive __contains, that returns True
        # if val is in the subtree starting at root, and False otherwise
        if root is None:
            return False
        elif root.getVal() == val:
            return True
        if val < root.val:
            return BinarySearchTree.__contains(root.getLeft(),val)
        if val > root.val:
            return BinarySearchTree.__contains(root.getRight(),val)
 
def main():
    #s = input("Enter a list of numbers: ")
    #s = "22 3 4 33 1 2 1 45 5 6"
    s = "1 3 5 7 8 10 13"
    lst = s.split()
    
    tree = BinarySearchTree()
    
    for x in lst:
        tree.insert(float(x))
        
    for x in tree:
        print(x)

    print("min",tree.min())
    print("max",tree.max())
    print("removing",tree.remove(1))
    for x in tree:
        print(x)
    print("Contains", tree.__contains__(1))


if __name__ == "__main__":
    main()