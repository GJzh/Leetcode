# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node):
        if node == None: return (0, 0)
        ascending1 = ascending2 = descending1 = descending2 = 0
        x1, y1 = self.dfs(node.left)
        x2, y2 = self.dfs(node.right)
        if x1 and node.val == node.left.val + 1:
            ascending1 = x1
        if x2 and node.val == node.right.val + 1:
            ascending2 = x2
        if y1 and node.val == node.left.val - 1:
            descending1 = y1
        if y2 and node.val == node.right.val - 1:
            descending2 = y2
        self.ans = max(self.ans, 1 + max(ascending1 + descending2, ascending2 + descending1))
        return (1 + max(ascending1, ascending2), 1 + max(descending1, descending2))
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.dfs(root)
        return self.ans