# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath = float('-inf')
        self.dfs(root)
        return self.maxPath
    
    def dfs(self, node):
        if node == None: return 0
        a = self.dfs(node.left)
        b = self.dfs(node.right)
        self.maxPath = max(self.maxPath, node.val+max(a,b), node.val+a+b, node.val)
        return (node.val + max(a, b, 0))

