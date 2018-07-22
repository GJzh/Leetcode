class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2: return 0
        curProfit = 0
        profit = 0
        buy = prices[0]
        sell = prices[0]
        for i in range(1, len(prices)):
            if (prices[i] - buy - fee) > curProfit:
                curProfit = (prices[i] - buy - fee)
                sell = prices[i]
            buy = min(buy, prices[i])
            if (sell - prices[i] - fee >= 0):
                profit += curProfit
                curProfit = 0
                buy = prices[i]
                sell = prices[i]
        return profit + curProfit

