class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        dp1[i] = nums[0] * ... * nums[i-1]
        dp2[i] = nums[i] * ... * nums[n-1]
        """
        n = len(nums)
        if n < 2: return 0
        dp1 = [1] * (n+1)
        dp2 = [1] * (n+1)
        for i in range(1,n+1):
            dp1[i] = dp1[i-1] * nums[i-1]
        for i in range(n-1,-1,-1):
            dp2[i] = dp2[i+1] * nums[i]
        res = [0] * n
        for i in range(n):
            res[i] = dp1[i] * dp2[i+1]
        return res