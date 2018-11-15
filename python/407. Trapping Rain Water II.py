class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        if m == 0: return 0
        n = len(heightMap[0])
        if n == 0: return 0
        q = []
        visited = {}
        for j in range(n):
            heapq.heappush(q, (heightMap[0][j], 0, j))
            heapq.heappush(q, (heightMap[m-1][j], m-1, j))
            visited[(0, j)] = True
            visited[(m-1, j)] = True
        for i in range(1, m-1):
            heapq.heappush(q, (heightMap[i][0], i, 0))
            heapq.heappush(q, (heightMap[i][n-1], i, n-1))
            visited[(i, 0)] = True
            visited[(i, n-1)] = True
        maxHeight = float('-inf')
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        ans = 0
        while len(q):
            height, i, j = heapq.heappop(q)
            maxHeight = max(maxHeight, height)
            for direction in directions:
                x = i + direction[0]
                y = j + direction[1]
                if x >= 0 and x < m and y >= 0 and y < n and (x,y) not in visited:
                    visited[(x,y)] = True
                    heapq.heappush(q, (heightMap[x][y], x, y))
                    ans += max(0, (maxHeight - heightMap[x][y]))
        return ans