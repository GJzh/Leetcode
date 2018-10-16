class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = {}
        for c in s:
            if c not in freq: freq[c] = 1
            else: freq[c] += 1
        cnt = 0
        for key, value in freq.items():
            if value & 1: cnt += 1
        return cnt <= 1