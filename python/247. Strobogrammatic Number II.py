class Solution(object):
    def findStrobogrammatic(self, n):
        return self._findStrobogrammatic(n, n)
    
    def _findStrobogrammatic(self, m, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if m == 0: return [""]
        if m == 1: return ["0", "1", "8"]
        cur = self._findStrobogrammatic(m-2, n)
        res = []
        for word in cur:
            if m != n:
                res.append("0" + word + "0")
            res.append("1" + word + "1")
            res.append("8" + word + "8")
            res.append("6" + word + "9")
            res.append("9" + word + "6")
        return res