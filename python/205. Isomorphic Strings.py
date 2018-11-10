class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        status1 = {}
        status2 = {}
        for i in range(len(s)):
            if s[i] not in status1 and t[i] not in status2:
                status1[s[i]] = t[i]
                status2[t[i]] = s[i]
            elif s[i] in status1 and t[i] in status2:
                if status1[s[i]] != t[i] or status2[t[i]] != s[i]:
                    return False
            else:
                return False
        return True