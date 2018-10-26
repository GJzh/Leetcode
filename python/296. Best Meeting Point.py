class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        sort the house positions
        For one dimension space, the best meeting positions (multiple) should be in the middle of houses
        the sum distance is then (houses[n-1] - houses[0]) + (houses[n-2] - houses[1]) + ... 
        Fortunately, for Manhattan distance, we can process different dimensions separately
        Therefore, we should sum the distance along the two dimensions
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        rows = []
        cols = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        left, right = 0, len(rows)-1
        distance = 0
        while left < right:
            distance += (rows[right] - rows[left]) + (cols[right] - cols[left]) 
            left += 1
            right -= 1
        return distance