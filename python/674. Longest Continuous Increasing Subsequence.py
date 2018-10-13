class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return n
        left, right = 0, 1
        res = 1
        while right < n:
            while right < n and nums[right] > nums[right-1]:
                right += 1
            res = max(res, right - left)
            while right < n and nums[right] <= nums[right-1]:
                right += 1
            left = right - 1
        return res