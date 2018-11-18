class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        sums = [0] * n
        sums[0] = nums[0]
        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i]
        dp = [[float('inf') for j in range(n)] for i in range(m)]
        for j in range(n): dp[0][j] = sums[j]
        for i in range(1, m):
            for j in range(i, n):
                for k in range(i, j+1):
                    diff = sums[j] - sums[k-1]
                    if diff >= dp[i][j]: break
                    dp[i][j] = min(dp[i][j], max(dp[i-1][k-1], diff) )
        return dp[m-1][n-1]