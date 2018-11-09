class Solution(object):
    class UnionFind():
        def __init__(self, K, n):
            self.v = [k for k in range(K)]
            self.sz = [1] * K
            self.n = n
            
        def find(self, k):
            while k != self.v[k]:
                self.v[k] = self.v[self.v[k]]
                k = self.v[k]
            return k
            
        def merge(self, k1, k2):
            '''
            return the number of bricks that are added into the tree connected to the top
            '''
            k1 = self.find(k1)
            k2 = self.find(k2)
            if k1 == k2: return 0
            if k1 < self.n and k2 >= self.n:
                self.v[k2] = k1
                self.sz[k1] += self.sz[k2]
                return self.sz[k2]
            elif k2 < self.n and k1 >= self.n:
                self.v[k1] = k2
                self.sz[k2] += self.sz[k1]
                return self.sz[k1]
            elif self.sz[k1] < self.sz[k2]:
                self.v[k1] = k2
                self.sz[k2] += self.sz[k1]
                return 0
            else:
                self.v[k2] = k1
                self.sz[k1] += self.sz[k2]
                return 0
                
    def valid(self, x, y, m, n):
        return x >= 0 and x < m and y >= 0 and y < n
        
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # remove the hited bricks
        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = -1
        # find connected components
        p = self.UnionFind(m * n, n)
        for x in range(m):
            for y in range(n):
                if grid[x][y] != 1: continue
                idx = x * n + y
                if self.valid(x+1, y, m, n) and grid[x+1][y] == 1:
                    p.merge(idx, (x+1) * n + y )
                if self.valid(x, y+1, m, n) and grid[x][y+1] == 1:
                    p.merge(idx, x * n + (y + 1) )
        # find droped bricks
        ans = [0] * len(hits)
        for i in range(len(hits)-1, -1, -1):
            x, y = hits[i]
            idx = x * n + y
            if grid[x][y] == 0: continue
            cnt = 0
            for dx, dy in directions:
                a, b = x + dx, y + dy
                if self.valid(a, b, m, n) and grid[a][b] == 1:
                    num = p.merge(idx, a * n + b)
                    if p.find(idx) < n: cnt += num
            grid[x][y] = 1
            # do not count the hitted brick grid[x][y]
            ans[i] = max(0, cnt-1) if idx >= n else cnt
        return ans