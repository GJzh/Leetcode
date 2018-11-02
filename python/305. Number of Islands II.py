Solution: Weighted Union Find, time: O(klog(m*n)) space(m*n)
class Solution(object):
    class Islands():
        def __init__(self, m, n):
            self.islands = [0] * (m * n)
            self.sz = [1] * (m * n)
            self.m = m
            self.n = n
            self.islands = [k for k in range(m*n)]
        
        def find(self, pos):
            k = self.n * pos[0] + pos[1]
            while self.islands[k] != k:
                self.islands[k] = self.islands[self.islands[k]]
                k = self.islands[k]
            return k
        
        def merge(self, pos1, pos2):
            k1 = self.find(pos1)
            k2 = self.find(pos2)
            if k1 == k2: return False
            if self.sz[k1] < self.sz[k2]:
                self.islands[k1] = k2
                self.sz[k2] += self.sz[k1]
            else:
                self.islands[k2] = k1
                self.sz[k1] += self.sz[k2]
            return True
    
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0 for j in range(n)] for i in range(m)]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        p = self.Islands(m, n)
        cnt = 0
        res = []
        for x, y in positions:
            if grid[x][y] == 1: 
                res.append(cnt)
                continue
            grid[x][y] = 1
            cnt += 1
            for direction in directions:
                a, b = x + direction[0], y + direction[1]
                if a >= 0 and a < m and b >= 0 and b < n and grid[a][b] == 1 and p.merge([x,y], [a,b]):
                    cnt -= 1
            res.append(cnt)
        return res