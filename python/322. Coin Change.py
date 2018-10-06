class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0: break
                dp[i] = min(dp[i], 1+dp[i - coin])
        return dp[amount] if dp[amount] != float('inf') else -1