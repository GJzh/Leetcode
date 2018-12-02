class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        n = len(S)
        dp = [1]
        for i in range(1, n+1):
            temp = [0] * (i+1)
            cur = 0
            if S[i-1] == 'D':
                for j in range(i-1, -1, -1):
                    cur += dp[j]
                    temp[j] = cur
            else:
                for j in range(1, i+1):
                    cur += dp[j-1]
                    temp[j] = cur
            dp = temp
        return sum(dp) % mod