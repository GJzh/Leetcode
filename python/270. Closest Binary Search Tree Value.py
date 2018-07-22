# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.dfs(root, target, root.val)
    
    def dfs(self, node, target, candidate):
        if node == None:
            return candidate
        if node.val == target:
            return node.val
        if abs(target - node.val) < abs(target - candidate):
            candidate = node.val    
        if target < node.val:
            return self.dfs(node.left, target, candidate)
        else:
            return self.dfs(node.right, target, candidate)
