class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        diction = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        n = len(s)
        res = 0
        cnt = 0
        prev = 10000
        for c in s:
            num = diction[c]
            if num == prev: cnt += num
            elif num < prev:
                res += cnt
                cnt = num
                prev = num
            else:
                res -= cnt
                cnt = num
                prev = num
        res += cnt
        return res

