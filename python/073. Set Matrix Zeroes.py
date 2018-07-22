class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = False
        first_column = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_column = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_column:
            for i in range(m):
                matrix[i][0] = 0

