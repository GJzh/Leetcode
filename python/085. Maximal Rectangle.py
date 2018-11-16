class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        heights = [0] * (n + 1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            q = []
            for j in range(n+1):
                while len(q) and heights[q[-1]] >= heights[j]:
                    height = heights[q[-1]]
                    q.pop()
                    width = j - q[-1] - 1 if len(q) else j
                    ans = max(ans, height * width)
                q.append(j)
        return ans