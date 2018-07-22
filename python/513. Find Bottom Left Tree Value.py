Solution1 BFS:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur = [root]
        res = root 
        while len(cur) > 0:
            temp = []
            for node in cur:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            if len(temp) > 0: res = temp[0]
            cur = temp
        return res.val

Solution 2 DFS:
class Solution:
    def dfs(self, node, level):
        if not node: return
        if level > self.level:
            self.res = node
            self.level = level
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)
            
    
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.level = 0
        self.res = root
        self.dfs(root, 1)
        return self.res.val

