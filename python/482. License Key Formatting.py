class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        n = len(S)
        if n == 0: return ""
        l = n % K
        idx = 0
        ans = S[:l]
        if len(ans) > 0: ans += "-"
        for i in range(1, n/K+1):
            ans += S[l+(i-1)*K:l+i*K]
            ans += "-"
        return ans[:len(ans)-1]