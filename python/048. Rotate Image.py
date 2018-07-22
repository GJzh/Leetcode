class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2: return
        K = n // 2
        for k in range(K):
            for j in range(n-2*k-1):
                num = matrix[k][k+j]
                matrix[k][k+j] = matrix[n-k-1-j][k]
                matrix[n-k-1-j][k] = matrix[n-k-1][n-k-1-j]
                matrix[n-k-1][n-k-1-j] = matrix[k+j][n-k-1]
                matrix[k+j][n-k-1] = num

