class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        if n == 0: return
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.BIT2D = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        m = len(self.matrix)
        n = len(self.matrix[0])
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= m:
            j = col + 1
            while j <= n:
                self.BIT2D[i][j] += diff
                j += (j & (-j))
            i += (i & (-i))

    def getSum(self, row, col):
        ans = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                ans += self.BIT2D[i][j]
                j -= (j & (-j))
            i -= (i & (-i))
        return ans
            
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getSum(row2, col2) - self.getSum(row2, col1-1) - self.getSum(row1-1, col2) + self.getSum(row1-1, col1-1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)