class Solution:
    # @return a string
    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return l+1, r-1
    def longestPalindrome(self, s):
        start = end = 0
        for i in range(len(s)):
            l, r = self.getlongestpalindrome(s, i, i)
            if r - l > end - start:
                start = l
                end = r
            l, r = self.getlongestpalindrome(s, i, i + 1)
            if r - l > end - start: 
                start = l
                end = r
        return s[start:end+1]

