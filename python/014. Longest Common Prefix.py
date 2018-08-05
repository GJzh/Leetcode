class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        n = sys.maxsize
        for s in strs:
            n = min(n, len(s))
        res = ""
        for i in range(n):
            cur = strs[0][i]
            for s in strs:
                if s[i] != cur: return res
            res += cur
        return res
