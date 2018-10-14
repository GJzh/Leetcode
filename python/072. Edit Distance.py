class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        dp[i][j] the distance between word1[:i] and word2[:j], res = dp[m][n]
        """
        m = len(word1)
        n = len(word2)
        if m == 0 and n == 0: return 0
        elif m == 0: return n
        elif n == 0: return m
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(1, n+1): dp[0][j] = j
        for i in range(1, m+1): dp[i][0] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[m][n]