class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if n > m: return -1
        if n == 0: return 0
        for i in range(m-n+1):
            flag = True
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag: return i
        return -1

