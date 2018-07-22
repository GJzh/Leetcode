class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        if n == 0: return []
        K = min(m, n) // 2
        res = []
        for k in range(K):
            res += [matrix[k][j] for j in range(k,n-k-1) ]
            res += [matrix[i][n-k-1] for i in range(k,m-1-k)]
            res += [matrix[m-1-k][j] for j in range(n-1-k,k,-1)]
            res += [matrix[i][k] for i in range(m-k-1,k,-1)]
        if m <= n and m % 2 == 1:
            res += [matrix[K][j] for j in range(K,n-K)]
        elif n <= m and n % 2 == 1:
            res += [matrix[i][K] for i in range(K,m-K)]
        return res

