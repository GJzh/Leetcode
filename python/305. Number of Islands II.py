class Solution(object):
    class Islands():
        def __init__(self, m, n):
            self.islands = [0] * (m * n)
            self.m = m
            self.n = n
            for i in range(m):
                for j in range(n):
                    self.islands[i * n + j] = i * n + j
        
        def find(self, pos):
            k = self.n * pos[0] + pos[1]
            while self.islands[k] != k:
                k = self.islands[k]
            return k
        
        def merge(self, pos1, pos2):
            k1 = self.find(pos1)
            k2 = self.find(pos2)
            self.islands[k1] = k2
    
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0 for j in range(n)] for i in range(m)]
        p = self.Islands(m, n)
        cnt = 0
        res = []
        for x, y in positions:
            if grid[x][y] == 1: continue
            grid[x][y] = 1
            cnt += 1
            if x-1 >= 0 and grid[x-1][y] == 1 and p.find([x,y]) != p.find([x-1,y]):
                p.merge([x,y], [x-1,y])
                cnt -= 1
            if x+1 < m and grid[x+1][y] == 1 and p.find([x,y]) != p.find([x+1,y]):
                p.merge([x,y], [x+1,y])
                cnt -= 1  
            if y-1 >= 0 and grid[x][y-1] == 1 and p.find([x,y]) != p.find([x,y-1]):
                p.merge([x,y], [x,y-1])
                cnt -= 1
            if y+1 < n and grid[x][y+1] == 1 and p.find([x,y]) != p.find([x,y+1]):
                p.merge([x,y], [x,y+1])
                cnt -= 1 
            res.append(cnt)
        return res