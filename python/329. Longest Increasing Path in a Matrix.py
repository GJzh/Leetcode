class Solution(object):
    def dfs(self, i, j):
        if self.status[i][j] > 0: return self.status[i][j]
        self.status[i][j] = 1
        if i-1 >= 0 and self.matrix[i][j] < self.matrix[i-1][j]:
            self.status[i][j] = max(self.status[i][j], 1 + self.dfs(i-1, j))
        if i+1 < len(self.matrix) and self.matrix[i][j] < self.matrix[i+1][j]:
            self.status[i][j] = max(self.status[i][j], 1 + self.dfs(i+1, j))
        if j-1 >= 0 and self.matrix[i][j] < self.matrix[i][j-1]:
            self.status[i][j] = max(self.status[i][j], 1 + self.dfs(i, j-1))
        if j+1 < len(self.matrix[0]) and self.matrix[i][j] < self.matrix[i][j+1]:
            self.status[i][j] = max(self.status[i][j], 1 + self.dfs(i, j+1))
        return self.status[i][j]
    
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix = matrix
        m = len(matrix)
        if not m: return 0
        n = len(matrix[0])
        if not n: return 0
        self.status = [[0 for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(i, j))
        return res
