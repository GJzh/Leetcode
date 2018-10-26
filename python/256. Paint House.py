class Solution(object):
    def update(self, status, idx):
        m = len(status)
        res = [float('inf')] * m
        for i in range(m):
            for j in range(m):
                if i == j: continue
                res[i] = min(res[i], self.costs[idx][i] + status[j])
        return res
    
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0: return 0
        m = 3
        status = [0] * m
        self.costs = costs
        for i in range(n):
            status = self.update(status, i)
        return min(status)