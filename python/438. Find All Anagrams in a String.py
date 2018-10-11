class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        status = {}
        for c in p:
            if c not in status:
                status[c] = 1
            else:
                status[c] += 1
        cnt = len(status)
        left, right = 0, 0
        res = []
        while right < len(s):
            while right < len(s) and right - left < len(p):
                if s[right] in status:
                    status[s[right]] -= 1
                else:
                    status[s[right]] = -1
                if status[s[right]] == 0:
                    cnt -= 1
                elif status[s[right]] == -1:
                    cnt += 1
                right += 1
            if cnt == 0: res.append(left)
            if right - left == len(p):
                status[s[left]] += 1
                if status[s[left]] == 0:
                    cnt -= 1
                elif status[s[left]] == 1:
                    cnt += 1
                left += 1
        return res