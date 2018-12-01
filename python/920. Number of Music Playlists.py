class Solution(object):    
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        if N > L: return 0
        dp = [0] * (N+1)
        dp[0] = 1
        for i in range(L):
            temp = [0] * (N+1)
            for j in range(1, min(N, i+1)+1):
                temp[j] = dp[j-1] * (N - j + 1) + dp[j] * max(0, j - K)
            dp = temp
        return dp[N] % mod