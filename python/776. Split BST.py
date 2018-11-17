# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if root == None: return [None, None]
        leftTree, rightTree = TreeNode(0), TreeNode(0)
        leftNode, rightNode = leftTree, rightTree
        node = root
        while node:
            if node.val == V:
                leftNode.right = node
                rightNode.left = node.right
                node.right = None
                node = None
            elif node.val < V:
                leftNode.right = node
                leftNode = node
                temp = node.right
                leftNode.right = None
                node = temp
            else:
                rightNode.left = node
                rightNode = node
                temp = node.left
                rightNode.left = None
                node = temp
        return [leftTree.right, rightTree.left]