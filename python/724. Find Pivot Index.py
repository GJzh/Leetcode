class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return -1
        total = 0
        for num in nums:
            total += num
        left = 0
        for i in range(n):
            if left == total - left - nums[i]:
                return i
            left += nums[i]
        return -1