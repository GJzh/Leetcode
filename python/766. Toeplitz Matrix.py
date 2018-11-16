class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for k in range(1-m, n):
            cur = None
            for x in range(max(0, -k), min(n-k, m)):
                y = x + k
                if cur == None:
                    cur = matrix[x][y]
                if matrix[x][y] != cur:
                    return False
        return True