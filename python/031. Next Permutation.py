class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx1 = n-1
        # find the first (backwards) idx1 such that nums[idx1] > nums[idx1-1]
        while idx1 > 0 and nums[idx1] <= nums[idx1-1]:
            idx1 -= 1
        if idx1 > 0:
            # find the first (backwards) idx2 such that nums[idx2] > nums[idx1-1]
            idx2 = n-1
            while idx2 > idx1 and nums[idx2] <= nums[idx1-1]:
                idx2 -= 1
            nums[idx1-1], nums[idx2] = nums[idx2], nums[idx1-1]
        # sort nums[idx1:]
        for i in range((n-idx1)/2):
            nums[idx1+i], nums[n-1-i] = nums[n-1-i], nums[idx1+i]