class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        self.grid = grid
        cnt = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == '1':
                    cnt += 1
                    self.dfs(i,j)
        return cnt
    
    def dfs(self, i, j):
        m = len(self.grid)
        n = len(self.grid[0])
        self.grid[i][j] = '-'
        if i-1 >= 0 and self.grid[i-1][j] == '1':
            self.dfs(i-1,j)
        if i+1 < m and self.grid[i+1][j] == '1':
            self.dfs(i+1,j)
        if j-1 >= 0 and self.grid[i][j-1] == '1':
            self.dfs(i,j-1)
        if j+1 < n and self.grid[i][j+1] == '1':
            self.dfs(i,j+1)

