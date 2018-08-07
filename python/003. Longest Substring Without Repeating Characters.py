class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        maxCnt = 0
        left = right = 0
        status = {}
        n = len(s)
        while right < n:
            while right < n and s[right] not in status:
                status[s[right]] = True
                right += 1
            cnt = right - left
            if cnt > maxCnt:
                maxCnt = cnt 
            if right < n:
                while s[left] != s[right]:
                    del status[s[left]]
                    left += 1
                left += 1
                right += 1
        return maxCnt
