Solution 1: DP, time: O(m * n), space: O(m * n)
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        dp[i][j]: the start position of Minimum Window Subsequence for S[:i] and T[:j]
        """
        m = len(S)
        n = len(T)
        dp = [[-1 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        length = float('inf')
        ans = ""
        for i in range(1, m+1):
            for j in range(1, n+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
                if dp[i][n] != -1 and i - dp[i][n] < length:
                    length = i - dp[i][n]
                    ans = S[dp[i][n]:i]
        return ans
    
Solution 2: Two pointers, time: O(m * ans), space: O(1)
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        dp[i][j]: the start position of Minimum Window Subsequence for S[:i] and T[:j]
        """
        m = len(S)
        n = len(T)
        length = float('inf')
        idx1, idx2 = 0, 0
        ans = ""
        while idx1 < m:
            if S[idx1] == T[idx2]:
                idx2 += 1
                if idx2 == n:
                    start, end = idx1, idx1+1
                    idx2 -= 1
                    while idx2 >= 0:
                        if S[start] == T[idx2]:
                            idx2 -= 1
                        start -= 1
                    start += 1
                    if end - start < length:
                        length = end - start
                        ans = S[start:end]
                    idx1 = start
                    idx2 = 0
            idx1 += 1
        return ans