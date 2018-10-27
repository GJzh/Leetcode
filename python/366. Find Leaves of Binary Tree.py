# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, res):
        if node == None: return -1
        l = float('-inf')
        if node.left == None and node.right == None:
            l = 0
        else:
            if node.left:
                l1 = self.dfs(node.left, res)
                l = max(l, l1 + 1)
            if node.right:
                l2 = self.dfs(node.right, res)
                l = max(l, l2 + 1)
        if l == len(res):
            res.append([])
        res[l].append(node.val)
        return l
    
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, res)
        return res