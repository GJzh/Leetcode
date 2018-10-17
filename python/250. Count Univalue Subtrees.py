# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node):
        """
        :type root: TreeNode
        :rtype: bool, int
        """
        flag = True
        if node.left:
            flag1, val1 = self.dfs(node.left)
            if flag1 == False or val1 != node.val:
                flag = False
        if node.right:
            flag2, val2 = self.dfs(node.right)
            if flag2 == False or val2 != node.val:
                flag = False
        if flag: self.res += 1
        return flag, node.val
        
    
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if root == None: return 0
        self.dfs(root)
        return self.res