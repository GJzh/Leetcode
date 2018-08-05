class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        status = {}
        for c in t:
            if c not in status:
                status[c] = 1
            else:
                status[c] += 1
        cnt = n
        left = 0
        right = 0
        window = ""
        l = m+1
        while right < m:
            while right < m and cnt > 0:
                if s[right] in status:
                    status[s[right]] -= 1
                    if status[s[right]] >= 0: cnt -= 1
                right += 1
            while left < right:
                if s[left] in status:
                    status[s[left]] += 1
                    if status[s[left]] > 0:
                        break
                left += 1
            if cnt == 0 and (right - left) < l:
                window = s[left:right]
                l = len(window)
            cnt += 1
            left += 1
                
        return window 
