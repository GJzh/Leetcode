class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf') for i in range(n+1)] for j in range(m+1)]
        dp[m][n-1] = dp[m-1][n] = 1
        for x in range(m-1,-1,-1):
            for y in range(n-1,-1,-1):
                dp[x][y] = max(1, min(dp[x+1][y], dp[x][y+1]) - dungeon[x][y])
        return dp[0][0]

