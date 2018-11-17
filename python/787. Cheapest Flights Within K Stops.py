class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        schedule = {}
        for s, t, price in flights:
            if (s, t) not in schedule:
                schedule[(s, t)] = price
            else:
                schedule[(s, t)] = min(schedule[(s, t)], price)
        dp = [float('inf')] * n
        dp[src] = 0
        stop = 0
        while stop < K + 1:
            temp = copy.copy(dp)
            cnt = 0
            for t in range(n):
                for s in range(n):
                    if dp[s] >= 0 and (s,t) in schedule:
                        price = dp[s] + schedule[(s,t)]
                        if price < temp[t]:
                            cnt += 1
                            temp[t] = price
            dp = temp
            if cnt == 0: break
            stop += 1
        return dp[dst] if dp[dst] != float('inf') else -1