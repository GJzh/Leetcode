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
            self.dp = None 
            return 
        n = len(matrix[0])
        if n == 0: 
            self.dp = None 
            return
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = matrix[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + matrix[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = matrix[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        self.dp = dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.dp == None: return [None]
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        elif row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        elif col1 == 0:
            return self.dp[row2][col2] - self.dp[row1-1][col2]
        else:
            return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]