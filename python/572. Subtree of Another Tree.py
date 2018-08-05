# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, s, t):
        if s == None and t == None: return True
        if s == None or t == None: return False
        if s.val != t.val: return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None and t == None: return True
        if s == None or t == None: return False
        if s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
