class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        vertbi decoding, dp[i] : the maximum Vacation Days if you stay at city i at the current week
        dp[prevCity] = -1 -> prevCity is not reachable
        """
        N = len(flights)
        K = len(days[0])
        dp = [0] * N
        for i in range(N):
            if i == 0 or flights[0][i]:
                dp[i] = days[i][0]
            else:
                dp[i] = -1
        for week in range(1,K):
            temp = [-1] * N
            for city in range(N):
                for prevCity in range(N):
                    if dp[prevCity] >= 0 and (prevCity == city or flights[prevCity][city]):
                        temp[city] = max(temp[city], dp[prevCity] + days[city][week])
            dp = temp    
        return max(dp)