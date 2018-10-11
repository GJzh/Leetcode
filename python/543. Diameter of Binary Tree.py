# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _diameterOfBinaryTree(self, node, res):
        if node == None: return 0
        a = self._diameterOfBinaryTree(node.left, res)
        b = self._diameterOfBinaryTree(node.right, res)
        res[0] = max(res[0], 1 + a + b)
        return (1 + max(a,b))
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        res = [0]
        self._diameterOfBinaryTree(root, res)
        return res[0]-1