class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        status = {}
        for c in t:
            if c not in status:
                status[c] = 1
            else:
                status[c] += 1
        cnt = len(status)
        left, right = 0, 0
        n = len(s)
        start = -1
        end = -1
        minL = float('inf')
        while right < n:
            # move right
            while right < n and cnt > 0:
                if s[right] in status:
                    status[s[right]] -= 1
                    if status[s[right]] == 0:
                        cnt -= 1
                right += 1
            if cnt > 0: break
            # move left
            while left < right and cnt == 0:
                if s[left] in status:
                    status[s[left]] += 1
                    if status[s[left]] > 0:
                        cnt += 1
                left += 1
            left -= 1
            # keep track of the minimum substring
            if right - left < minL:
                start, end = left, right
                minL = right - left
            left += 1
        return s[start:end] if start >= 0 else ""