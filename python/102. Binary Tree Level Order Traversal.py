# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        cur = [root]
        res = [] 
        while len(cur) > 0:
            temp = []
            nums = []
            for node in cur:
                nums.append(node.val)
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            cur = temp
            res.append(nums)
        return res

