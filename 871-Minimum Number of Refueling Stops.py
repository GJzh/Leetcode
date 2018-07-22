class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        n = len(stations)
        if n == 0: return 0 if startFuel >= target else -1
        dp = [0] * (n+1)
        dp[0] = startFuel
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):

                if dp[j] >= stations[i-1][0]:
                    dp[j+1] = max(dp[j] + stations[i-1][1], dp[j+1])
        for i in range(len(dp)):
            if dp[i] >= target: return i
        return -1
Solution 2:
class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        pq = []
        n = len(stations)
        cur = startFuel
        stops = 0
        i = 0
        while True:
            if cur >= target: return stops
            while i < n and stations[i][0] <= cur:
                heapq.heappush(pq, -stations[i][1])
                i += 1
                
            if not pq: break;
            cur -= heapq.heappop(pq)
            stops += 1
        return -1

