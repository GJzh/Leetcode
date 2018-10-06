# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node):
        if node == None: return float('-inf')
        leftSum = self.dfs(node.left)
        rightSum = self.dfs(node.right)
        self.res = max(self.res, max(0, leftSum) + max(0, rightSum) + node.val)
        return max(leftSum, rightSum, 0) + node.val
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = float('-inf')
        self.dfs(root)
        return self.res