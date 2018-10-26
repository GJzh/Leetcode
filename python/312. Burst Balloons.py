class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        nums = ([1] + nums + [1])
        dp = [[0 for j in range(n+2)] for i in range(n+2)]
        for l in range(1, n+1):
            for i in range(1, n-l+2):
                j = i + l - 1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], nums[k] * nums[i-1] * nums[j+1] + dp[i][k-1] + dp[k+1][j])
        return dp[1][n]