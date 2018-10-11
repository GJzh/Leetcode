class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        res = 0
        sums = [0] * n
        sums[0] = nums[0]
        for i in range(1,n):
            sums[i] = sums[i-1] + nums[i]
        status = {}
        status[0] = -1
        for i in range(n):
            if sums[i] - k in status:
                length = i - status[sums[i]-k]
                res = max(res, length)
            if sums[i] not in status:
                status[sums[i]] = i
        return res