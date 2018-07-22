class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = (n + 1) * n / 2
        for num in nums:
            cnt -= num
        return cnt

