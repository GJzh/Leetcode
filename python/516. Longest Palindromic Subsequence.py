Solution 1 (time: O(n^2), space: O(n^2))
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        dp[i][j]: the maximum length of Palindrom in s[i:j+1]
        dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j]
        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        dp[i][i] = 1
        """
        n = len(s)
        if n <= 1: return n
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][n-1]

Solution 2 (time: O(n^2), space: O(n))
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        dp[i]: dp[i][j-1]
        temp[i]: dp[i][j]
        """
        n = len(s)
        if n <= 1: return n
        for j in range(n):
            temp = [0] * (j+1)
            for i in range(j, -1, -1):
                if i == j:
                    temp[i] = 1
                elif j - i == 1:
                    temp[i] = 2 if s[i] == s[j] else 1
                elif s[i] == s[j]:
                    temp[i] = dp[i+1] + 2
                else:
                    temp[i] = max(temp[i+1], dp[i])
            dp = temp
        return dp[0]