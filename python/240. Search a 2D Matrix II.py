class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if not m: return False
        n = len(matrix[0])
        if not n: return False
        x = m-1
        y = 0
        while x >= 0 and y < n:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                y += 1
            else:
                x -= 1
        return False