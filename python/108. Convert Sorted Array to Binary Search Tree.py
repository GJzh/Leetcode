# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, nums, left, right):
        if left > right: return None
        mid = (left + right) / 2
        node = TreeNode(nums[mid])
        node.left = self.buildTree(nums, left, mid-1)
        node.right = self.buildTree(nums, mid+1, right)
        return node
        
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0: return None
        return self.buildTree(nums, 0, n-1)