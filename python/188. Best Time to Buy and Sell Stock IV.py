class Solution(object):
    def _maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
    
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n/2:
            return self._maxProfit(prices)
        dp = [[0 for i in range(n)] for j in range(k+1)]
        for i in range(1,k+1):
            maxTemp = -prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], maxTemp + prices[j])
                maxTemp = max(maxTemp, dp[i-1][j-1] - prices[j])
        return dp[k][n-1]
