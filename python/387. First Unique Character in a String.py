class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        visited = [n] * 26
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if visited[idx] == n:
                visited[idx] = i
            elif visited[idx] < n:
                visited[idx] = n+1
        res = n
        for i in range(26):
            if visited[i] < n: res = min(res, visited[i])
        return res if res < n else -1

