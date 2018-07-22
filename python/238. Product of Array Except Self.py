class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dp1 = [1]
        dp2 = [1]
        for i in range(n):
            dp1.append(dp1[-1] * nums[i])
        for j in range(n-1,-1,-1):
            dp2.append(dp2[-1] * nums[j])
        res = []
        for k in range(n):
            res.append(dp1[k] * dp2[n-k-1])
        return res

