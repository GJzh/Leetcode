class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        dp = [[0 for j in range(n+1)] for i in range(n+1)]
        for l in range(1,n):
            for i in range(1, n-l+1):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i,j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        return dp[1][n]