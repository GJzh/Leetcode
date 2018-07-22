# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, p):
        if not node: return
        if node.val == p.val:
            self.flag = True
            self.dfs(node.right, p)
            return
        if self.flag:
            self.res = node.val
            self.dfs(node.left, p)
        else:
            if p.val < node.val:
                self.res = node.val
                self.dfs(node.left, p)
            else:
                self.dfs(node.right, p)
    
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.res = None
        self.flag = False
        self.dfs(root, p)
        return self.res if self.flag else None

