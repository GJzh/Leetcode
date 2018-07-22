class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res = 26 * res + ord(c) - ord('A') + 1
        return res

