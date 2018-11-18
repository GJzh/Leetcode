class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [poured]
        for i in range(1, query_row+1):
            temp = [0] * (i+1)
            for j in range(i+1):
                if j > 0: temp[j] += max(0, (dp[j-1] - 1) / 2.0 )
                if j < i: temp[j] += max(0, (dp[j] - 1) / 2.0 )
            dp = temp
            if max(dp) == 0: return 0
        return min(1, dp[query_glass])