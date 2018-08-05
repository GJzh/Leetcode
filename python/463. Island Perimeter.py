class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        if not n: return 0
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] != 1:
                        cnt += 1
                    if i == m-1 or grid[i+1][j] != 1:
                        cnt += 1
                    if j == 0 or grid[i][j-1] != 1:
                        cnt += 1
                    if j == n-1 or grid[i][j+1] != 1:
                        cnt += 1  
        return cnt
