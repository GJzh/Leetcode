# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, level, res):
        if node == None: return
        if level >= len(res):
            res.append(node.val)
        self.dfs(node.right, level+1, res)
        self.dfs(node.left, level+1, res)
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, 0, res)
        return res