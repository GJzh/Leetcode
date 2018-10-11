# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, res):
        if node.left:
            self.dfs(node.left, res)
        if self.before.val > node.val:
            res.append(self.before)
            res.append(node)
        self.before = node
        if node.right:
            self.dfs(node.right, res)
        
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None: return
        res = []
        self.before = TreeNode(float('-inf'))
        self.dfs(root, res)
        res[0].val, res[-1].val = res[-1].val, res[0].val