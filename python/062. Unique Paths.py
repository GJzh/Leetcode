class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        dp[i]: the number of paths to grid[i][cur]
        time: O(m*n)
        space: O(min(m,n))
        """
        if n < m:
            return self.uniquePaths(n, m)
        dp = [1] * m
        for j in range(1,n):
            for i in range(1, m):
                dp[i] += dp[i-1]
        return dp[m-1]