class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxCnt = 0
        freq = [0] * 26
        start = 0
        ans = 0
        for i in range(len(s)):
            idx = ord(s[i]) - ord('A')
            freq[idx] += 1
            maxCnt = max(maxCnt, freq[idx])
            if i - start + 1 - maxCnt > k:
                freq[ord(s[start]) - ord('A')] -= 1
                start += 1
            ans = max(ans, i - start + 1)
        return ans