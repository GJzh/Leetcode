# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        ancestors = [root]
        for _ in range(d-2):
            temp = []
            for node in ancestors:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ancestors = temp
        for ancestor in ancestors:
            leftNode = TreeNode(v)
            rightNode = TreeNode(v)
            if ancestor.left:
                leftNode.left = ancestor.left
            if ancestor.right:
                rightNode.right = ancestor.right
            ancestor.left = leftNode
            ancestor.right = rightNode
        return root
