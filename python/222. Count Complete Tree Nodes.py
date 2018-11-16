# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
time: O((logn)^2)
class Solution(object):
    def getLeftHeight(self, node):
        cnt = 1
        while node.right:
            cnt += 1
            node = node.right
        return cnt
        
    def getRightHeight(self, node):
        cnt = 1
        while node.left:
            cnt += 1
            node = node.left
        return cnt
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        leftH = self.getLeftHeight(root)
        rightH = self.getRightHeight(root)
        if leftH == rightH: return 2 ** leftH - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1