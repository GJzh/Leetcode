from collections import defaultdict
class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        n = len(S)
        if n == 0: return 0
        ans = 2
        prevs = defaultdict(int)
        prevs[S[0]] = 1
        for i in range(1, n):
            temp = ans
            ans = 2 * ans - prevs[S[i]]
            prevs[S[i]] = temp
            ans %= mod
        return ans - 1 if ans >= 1 else mod - 1