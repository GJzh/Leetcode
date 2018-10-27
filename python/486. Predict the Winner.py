class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        dp[i][j]: the maximum score Player 1 can get from nums[i:j+1]
        sums[i] = nums[0] + nums[1] + ... nums[i-1]
        sums[j] - sums[i] = nums[i] + nums[i+1] + ... + nums[j-1]
        """
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n)]
        # initialize dp
        for i in range(n):
            dp[i][i] = nums[i]
        # calculate summations
        sums = [0] * (n+1)
        for i in range(n):
            sums[i+1] = sums[i] + nums[i]
        # update dp
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                total = sums[j+1] - sums[i]
                dp[i][j] = max(total - dp[i+1][j], total - dp[i][j-1])
                
        return dp[0][n-1] >= sums[n] / 2.0