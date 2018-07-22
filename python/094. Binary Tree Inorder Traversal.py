# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive:
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        a = b = []
        if root.left:
            a = self.inorderTraversal(root.left)
        if root.right:
            b = self.inorderTraversal(root.right)
        return a + [root.val] + b

# iteratively
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        if root == None: return []
        while root.left:
            stack.append(root)
            root = root.left
        res.append(root.val)
        while root.right or len(stack) > 0:
            if root.right:
                root = root.right
                while root.left:
                    stack.append(root)
                    root = root.left
            else:
                root = stack.pop()
            res.append(root.val)
        return res

