class Solution(object):
    def smaller(self, target):
        m = len(self.matrix)
        n = len(self.matrix[0])
        i, j = m-1, 0
        cnt = 0
        while i >= 0 and j < n:
            if self.matrix[i][j] <= target:
                cnt += (i+1)
                j += 1
            else:
                i -= 1
        return cnt
    
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        self.matrix = matrix
        m = len(self.matrix)
        if m == 0: return None
        n = len(self.matrix[0])
        if n == 0: return None
        left = matrix[0][0]
        right = matrix[m-1][n-1]
        while left <= right:
            mid = (left+right) / 2
            cnt = self.smaller(mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        return left