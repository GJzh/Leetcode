class NumMatrix(object):
    '''
    dp[i][j]: sum_{x=0}^{i}[sum_{y=0}^{j}matrix[x][y]]
    sumRegion(a ,b, c, d) = dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1]
    '''
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0: 
            self.sums = [0]
            return
        n = len(matrix[0])
        if n == 0: 
            self.sums = [0]
            return
        self.sums = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1]
        return
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2+1][col2+1] - self.sums[row2+1][col1] - self.sums[row1][col2+1] + self.sums[row1][col1]