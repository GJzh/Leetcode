class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while True:
            if left >= right: return True
            while left < right:
                if s[left].isalnum(): break
                else: left += 1
            while left <= right:
                if s[right].isalnum(): break
                else: right -= 1
            if left >= right: return True
            if s[left].lower() != s[right].lower(): return False
            left += 1
            right -= 1
        return True

