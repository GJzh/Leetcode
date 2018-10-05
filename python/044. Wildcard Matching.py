# Solution 1 (2 pointers):
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        idxs = 0
        idxp = 0
        idMatch = -1
        idStart = -1
        while idxs < m:
            if idxp < n and (s[idxs] == p[idxp] or p[idxp] == '?'):
                idxs += 1
                idxp += 1
            elif idxp < n and p[idxp] == '*':
                idMatch = idxp
                idStart = idxs
                idxp += 1
            elif idMatch >= 0:
                # p[idMatch] == '*'
                idxp = idMatch + 1
                idStart += 1
                idxs = idStart
            else:
                return False
        while idxp < n and p[idxp] == '*':
            idxp += 1
        return idxp == n and idxs == m

# Solution 2 (dp)
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        idxs = 0
        idxp = 0
        idMatch = -1
        idStart = -1
        while idxs < m:
            if idxp < n and (s[idxs] == p[idxp] or p[idxp] == '?'):
                idxs += 1
                idxp += 1
            elif idxp < n and p[idxp] == '*':
                idMatch = idxp
                idStart = idxs
                idxp += 1
            elif idMatch >= 0:
                idxp = idMatch + 1
                idStart += 1
                idxs = idStart
            else:
                return False
        while idxp < n and p[idxp] == '*':
            idxp += 1
        return idxp == n and idxs == m