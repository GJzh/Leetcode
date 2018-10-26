class Solution(object):
    def dfs(self, n, cur, res):
        if n == 1: return
        bound = int(math.floor(math.sqrt(n)))
        for i in range(2, bound + 1):
            if n % i == 0 and (len(cur) == 0 or i >= cur[-1]):
                cur.append(i)
                res.append(cur + [n/i])
                if math.sqrt(n / i) >= i:
                    self.dfs(n/i, cur, res)
                cur.pop()
        return
                
    
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        focus on combination, order doesn't matter
        to avoid duplication, I fix the order (non-decreasing) 2, 2, 3
        """
        cur = []
        res = []
        self.dfs(n, cur, res)
        return res