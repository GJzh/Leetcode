class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self._constructMaximumBinaryTree(0, len(nums)-1)
    
    def _constructMaximumBinaryTree(self, left, right):
        val = float('-inf')
        idx = -1
        for i in range(left,right+1):
            if self.nums[i] > val:
                val = self.nums[i]
                idx = i
        node = TreeNode(val)
        if idx > left:
            node.left = self._constructMaximumBinaryTree(left, idx-1)
        if idx < right:
            node.right = self._constructMaximumBinaryTree(idx+1, right)
        return node

