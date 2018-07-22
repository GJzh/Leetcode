# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.res = 1
        self._largestBSTSubtree(root)
        return self.res
        
    def _largestBSTSubtree(self, root):
        a1 = b2 = root.val
        b1 = root.val - 1
        a2 = root.val + 1
        num1 = num2 = 0
        flag1 = flag2 = True
        if root.left: a1, b1, num1, flag1 = self._largestBSTSubtree(root.left)
        if root.right: a2, b2, num2, flag2 = self._largestBSTSubtree(root.right)
        if flag1 and flag2 and b1 < root.val and a2 > root.val:
            self.res = max(self.res, 1+num1+num2)
            return a1, b2, 1+num1+num2, True
        else:
            return 0, 0, 0, False

