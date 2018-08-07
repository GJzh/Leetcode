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

class Solution:
    def _buildTree(self, l1, r1, l2, r2):
        if l1 > r1: return None
        node = TreeNode(self.postorder[r2])
        idx = self.pos[self.postorder[r2]]
        node.left = self._buildTree(l1, idx-1, l2, l2+idx-l1-1)
        node.right = self._buildTree(idx+1, r1, l2+idx-l1, r2-1)
        return node
        
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        length = len(inorder)
        if length == 0: return None
        self.inorder = inorder
        self.postorder = postorder
        self.pos = {}
        for i in range(length):
            self.pos[inorder[i]] = i
        return self._buildTree(0, length-1, 0, length-1)
