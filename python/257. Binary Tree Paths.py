# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, cur, res):
        if node.left == None and node.right == None:
            res.append(copy.copy(cur) + str(node.val))
            return
        size = len(cur)
        cur += (str(node.val) + "->")
        if node.left:
            self.dfs(node.left, cur, res)
        if node.right:
            self.dfs(node.right, cur, res)
        cur = cur[:size]
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None: return []
        cur = ""
        res = []
        self.dfs(root, cur, res)
        return res