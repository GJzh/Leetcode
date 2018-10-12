class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left