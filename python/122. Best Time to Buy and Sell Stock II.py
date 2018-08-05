class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2: return 0
        i = 1
        profit = 0
        while i < n:
            while i < n and prices[i] < prices[i-1]:
                i += 1
            if i < n: buy = prices[i-1]
            else: break
            while i < n and prices[i] >= prices[i-1]:
                i += 1
            sell = prices[i-1]
            profit += sell - buy
        return profit

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2: return 0
        buy = prices[0]
        sell = prices[0]
        curProfit = 0
        profit = 0
        for i in range(1,n):
            price = prices[i]
            buy = min(buy, price)
            sell = max(sell, price)
            curProfit = max(curProfit, price - buy)
            if price < sell:
                profit += curProfit
                buy = price
                sell = price
                curProfit = 0
        profit += curProfit
        return profit
