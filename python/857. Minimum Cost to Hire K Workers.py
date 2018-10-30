class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        n = len(quality)
        if n == 0: return 0.0
        workers = [(1.0 * wage[i] / quality[i], quality[i]) for i in range(n)]
        workers.sort()
        ans = float('inf')
        qualitySum = 0
        pq = []
        for r, q in workers:
            heapq.heappush(pq, -q)
            qualitySum += q
            
            if len(pq) > K:
                qualitySum += pq[0]
                heapq.heappop(pq)
            if len(pq) == K: ans = min(ans, r * qualitySum)
        return ans