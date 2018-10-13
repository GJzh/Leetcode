class Solution(object):    
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        dp[i]: hashtable dp[i][diff]: # of subsequence (1) end with A[i] and (2) difference is diff
        dp[j][diff] = a -> dp[i][diff] += (1 + a), res += a because the length of the subsequence must be > 2
        (1 + a): 1 length-2 subsequence, a length-k subsequence where k >= 3 (these subsequence ends at A[i])
        """
        n = len(A)
        if n < 3: return 0
        dp = [{} for i in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                num = dp[j][diff] + 1 if diff in dp[j] else 1
                if diff not in dp[i]:
                    dp[i][diff] = num
                else:
                    dp[i][diff] += num
                res += (num - 1)
        return res