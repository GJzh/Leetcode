class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows < 2: return s
        rows = ["" for _ in range(numRows)]
        k = 2 * (numRows - 1)
        idx = 0
        while idx < n:
            if idx % k == 0:
                i = 0
                while i < numRows and idx < n:
                    rows[i] += s[idx]
                    idx += 1
                    i += 1
            else:
                i = k - idx % k
                rows[i] += s[idx]
                idx += 1
        return "".join(rows)