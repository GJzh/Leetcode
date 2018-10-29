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
        ans = []
        if l > 0: ans.append(S[:l])
        for i in range(1, n/K+1):
            ans.append(S[l+(i-1)*K:l+i*K])
        return "-".join(ans)