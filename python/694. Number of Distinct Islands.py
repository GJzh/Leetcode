class Solution(object):
    def dfs(self, pos, island, offset):
        island.append(str(pos[0]-offset[0]))
        island.append(str(pos[1]-offset[1]))
        m = len(self.grid)
        n = len(self.grid[0])
        for direction in self.directions:
            x = pos[0] + direction[0]
            y = pos[1] + direction[1]
            if x >= 0 and x < m and y >= 0 and y < n and self.grid[x][y] == 1:
                self.grid[x][y] = 0
                self.dfs((x,y), island, offset)
        return
                
    
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        islands = {}
        self.grid = grid
        self.directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                offset = (i,j)
                island = []
                self.dfs((i,j), island, offset)
                island = ":".join(island)
                if island not in islands:
                    islands[island] = True
        return len(islands)
                