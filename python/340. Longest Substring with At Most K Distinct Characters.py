class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        n = len(s)
        ans = 0
        status = {}
        left, right = 0, 0
        while right < n:
            while right < n and len(status) <= k:
                if s[right] not in status: status[s[right]] = 1
                else: status[s[right]] += 1
                right += 1
            if len(status) <= k: return max(ans, right - left)
            right -= 1
            ans = max(ans, right - left)
            if right == n: break
            while left < right and len(status) > k:
                status[s[left]] -= 1
                if status[s[left]] == 0:
                    del status[s[left]]
                left += 1
            right += 1
        return ans