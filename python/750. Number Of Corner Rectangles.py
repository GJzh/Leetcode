class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        ans = 0
        for x1 in range(m-1):
            ones = []
            for z in range(n):
                if grid[x1][z]: ones.append(z)
            for x2 in range(x1+1, m):
                cnt = 0
                for y in ones:
                    if grid[x2][y]:
                        cnt += 1
                ans += cnt * (cnt - 1) / 2
        return ans