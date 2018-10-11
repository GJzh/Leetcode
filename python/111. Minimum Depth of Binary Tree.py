# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        cnt = 0
        cur = [root]
        while len(cur) > 0:
            cnt += 1
            temp = []
            for node in cur:
                if node.left == None and node.right == None: return cnt
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            cur = temp
        return cnt