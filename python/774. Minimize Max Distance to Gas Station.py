Solution 1: greedy algorithm, time: O(K)
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        stations.sort()
        q = []
        n = len(stations)
        for i in range(n-1):
            heapq.heappush(q, (stations[i]-stations[i+1], 1, i, i + 1))
        ans = q[0][0]
        while K:
            _, num, i, j = heapq.heappop(q)
            threshold = -q[0][0]
            cnt = int((stations[j] - stations[i]) / threshold) + 1
            x = min(K, cnt - num)
            K -= x
            heapq.heappush(q, (-1.0 * (stations[j] - stations[i]) / (num+x), num+x, i, j))
        return -q[0][0]

Solution 2: binary search, time: O(nlog(10^14))
class Solution(object):
    def valid(self, stations, distance, K):
        for i in range(len(stations)-1):
            K -= math.ceil((stations[i+1] - stations[i]) / distance) - 1
            if K < 0: return False
        return True
    
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        if len(stations) == 0: return 0
        stations.sort()
        left, right = 0, stations[-1] - stations[0]
        epsilon = 10 ** (-6)
        while abs(right - left) > epsilon:
            mid = (left + right) / 2.0
            if self.valid(stations, mid, K):
                right = mid - epsilon
            else:
                left = mid + epsilon
        return right
