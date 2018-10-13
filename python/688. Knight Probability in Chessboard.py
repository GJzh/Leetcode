from Queue import Queue
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K == 0: return 1
        directions = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        probs = [[0 for j in range(N)] for i in range(N)]
        probs[r][c] = 1.0
        q = set()
        q.add((r,c))
        for k in range(K):
            tempProbs =  [[0 for j in range(N)] for i in range(N)]
            tempQ = set()
            for r, c in list(q):
                for direction in directions:
                    x, y = r + direction[0], c + direction[1]
                    if x >= 0 and x < N and y >=0 and y < N:
                        tempProbs[x][y] += probs[r][c] / 8
                        tempQ.add((x,y))
            probs = tempProbs
            q = tempQ
            if len(q) == 0: break
        res = 0
        for x, y in list(q):
            res += probs[x][y]
        return res