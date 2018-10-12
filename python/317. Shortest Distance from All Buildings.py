from Queue import Queue
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return -1
        n = len(grid[0])
        if n == 0: return -1
        dist = [[0 for j in range(n)] for i in range(m)]
        directions = [[-1,0],[1,0],[0,-1],[0, 1]]
        flag = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                res = float('inf')
                q = Queue()
                q.put((i,j,0))
                while q.qsize() > 0:
                    a, b, d = q.get()
                    d += 1
                    for direction in directions:
                        x = a + direction[0]
                        y = b + direction[1]
                        if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == flag:
                            dist[x][y] += d
                            grid[x][y] -= 1
                            q.put((x,y,d))
                            res = min(res, dist[x][y])
                flag -= 1
        return -1 if res == float('inf') else res