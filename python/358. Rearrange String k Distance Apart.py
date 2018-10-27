time: O(n/k*logn)  space: O(n)
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k > 26: return ""
        if k == 0: return s
        freqs = [0] * 26
        for c in s:
            freqs[ord(c)-ord('a')] += 1
        v = []
        for i in range(26):
            v.append((freqs[i], chr(ord('a') + i)))
        v.sort()
        ans = ""
        while v[-1][0] > 0:
            for i in range(k):
                if v[25-i][0] <= 0: 
                    return ans if len(ans) == len(s) else ""
                ans += v[25-i][1]
                v[25-i] = (v[25-i][0]-1, v[25-i][1])
            v.sort()
        return ans if len(ans) == len(s) else ""