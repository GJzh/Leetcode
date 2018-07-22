class Solution:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N+1)
        dp[1] = 1
        for i in range(2,N+1):
            if i >= 4:
                for j in range(1,i-2):
                    dp[i] = max(dp[i], dp[j] * (i - j - 1) )
            dp[i] = max(dp[i], dp[i-1] + 1)
        return dp[N]

