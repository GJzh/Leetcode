class Solution(object):
    def _validPalindrome(self, s, start, end, cnt):
        if cnt > 1: return False
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                break
        if start == end or start == end + 1: return True
        return self._validPalindrome(s, start+1, end, cnt+1) or self._validPalindrome(s, start, end-1, cnt+1)
        
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self._validPalindrome(s, 0, len(s)-1, 0)