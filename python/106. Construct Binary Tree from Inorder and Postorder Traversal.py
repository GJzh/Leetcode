# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        length = len(inorder)
        if length == 0: return None
        if length == 1: return TreeNode(inorder[0])
        num = postorder[-1]
        idx = inorder.index(num)
        node = TreeNode(num)
        node.left = self.buildTree(inorder[:idx], postorder[:idx])
        node.right = self.buildTree(inorder[idx+1:], postorder[idx:length-1])
        return node

