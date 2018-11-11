class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        rows[i]: x = i
        cols[j]: y = j
        directional1[k]: x + y == k [0, m+n-2]
        directional2[k]: x - y == k - n + 1 [0, m+n-2]
        """
        m = len(M)
        if m == 0: return 0
        n = len(M[0])
        if n == 0: return 0
        rows = [0] * m
        cols = [0] * n
        directional1 = [0] * (m+n-1)
        directional2 = [0] * (m+n-1)
        ans = 0
        for x in range(m):
            for y in range(n):
                if M[x][y] == 1:
                    rows[x] += 1
                    cols[y] += 1
                    directional1[x + y] += 1
                    directional2[x - y + n - 1] += 1
                    ans = max(ans, rows[x], cols[y], directional1[x + y], directional2[x - y + n - 1])
                else:
                    rows[x] = 0
                    cols[y] = 0
                    directional1[x + y] = 0
                    directional2[x - y + n - 1] = 0
        return ans