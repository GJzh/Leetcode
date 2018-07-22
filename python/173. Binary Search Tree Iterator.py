# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.parents = []
        self.node = TreeNode(0)
        if root == None: self.node.right = None
        else:
            cur = root
            while cur.left:
                self.parents.append(cur)
                cur = cur.left
            self.node.right = cur
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.node.right: 
            self.node = self.node.right
            while self.node.left != None:
                self.parents.append(self.node)
                self.node = self.node.left
            return True
        elif len(self.parents)>0:
            self.node = self.parents.pop()
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        return self.node.val
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

