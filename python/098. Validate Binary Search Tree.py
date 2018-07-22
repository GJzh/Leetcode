# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        _, _, res = self._isValidBST(root)
        return res
        
        
    def _isValidBST(self, root):
        s = t = root.val
        flag = True
        if root.left:
            a, b, flag = self._isValidBST(root.left)
            if flag == False or b >= root.val: return None, None, False
            else: s = a
        if root.right:
            a, b, flag = self._isValidBST(root.right)
            if flag == False or a <= root.val: return None, None, False
            else: t = b
        return s, t, flag

