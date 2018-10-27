class Solution(object):    
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        keep track of two different colors is good enough
        """
        n = len(costs)
        if n == 0: return 0
        k = len(costs[0])
        if k == 0: return 0
        first = (float('inf'), -1)
        second = (float('inf'), -1)
        for i in range(k):
            if costs[0][i] < first[0]:
                second = first
                first = (costs[0][i], i)
            elif costs[0][i] < second[0]:
                second = (costs[0][i], i)
        for i in range(1, n):
            curFirst = (float('inf'), -1)
            curSecond = (float('inf'), -1)
            for j in range(k):
                if first[1] != j:
                    val = costs[i][j] + first[0]
                else:
                    val = costs[i][j] + second[0]
                if val < curFirst[0]:
                    curSecond = curFirst
                    curFirst = (val, j)
                elif val < curSecond[0]:
                    curSecond = (val, j)
            first = curFirst
            second = curSecond
        return first[0]