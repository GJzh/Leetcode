class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        visited = {}
        ans = 0
        left, right = 0, 0
        while right < n:
            while right < n and (len(visited) < 2 or s[right] in visited):
                if s[right] not in visited:
                    visited[s[right]] = 1
                else:
                    visited[s[right]] += 1
                right += 1
            ans = max(ans, right - left)
            if right >= n: break
            while left < right and len(visited) >= 2:
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    del visited[s[left]]
                left += 1
        return ans