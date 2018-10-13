class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if abs(m-n) > 1: return False
        if s == t: return False
        if abs(m-n) == 1 and (m * n) == 0: return True
        for i in range(min(m, n)):
            if s[i] != t[i]:
                if m == n:
                    return s[i+1:] == t[i+1:]
                elif m > n:
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
        return True