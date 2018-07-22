# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None: return None
        self._flatten(root)
        
    def _flatten(self, head):
        if head.left == None and head.right == None:
            return head
        else:
            node1 = node2 = None
            if head.left: node1 = self._flatten(head.left)
            if head.right: node2 = self._flatten(head.right)   
            if head.left:
                node1.right = head.right
                head.right = head.left
                head.left = None
        if node2:
            return node2
        else:
            return node1

