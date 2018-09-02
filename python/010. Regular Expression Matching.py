class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = [[False] * (m+1) for i in range(n+1)]
        dp[0][0] = True
        i = 1
        for j in range(2,m+1,2):
            dp[0][j] = dp[0][j-2] and p[j-1] == "*"
        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[j-1] == "*":
                    if j > 1:
                        if dp[i][j-2]:
                            dp[i][j] = True
                        elif dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'):
                            dp[i][j] = True
                        
                elif p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = (p[j-1] == s[i-1] and dp[i-1][j-1])
        return dp[n][m]
