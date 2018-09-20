class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2: return 0
        profits1 = [0] * n
        profits2 = [0] * n
        buy = prices[0]
        for i in range(1, n):
            profit = prices[i] - buy
            profits1[i] = max(profits1[i-1], profit)
            buy = min(buy, prices[i])
        sell = prices[n-1]
        for i in range(n-2, -1, -1):
            profit = sell - prices[i]
            profits2[i] = max(profits2[i+1], profit)
            sell = max(sell, prices[i])
        res = max(profits1[n-1], profits2[0])
        for i in range(1, n):
            res = max(res, profits1[i-1] + profits2[i])
        return res
