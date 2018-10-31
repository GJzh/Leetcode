class Solution(object):
    def _myPow(self, x, n):
        if n == 1: return x
        val1 = self._myPow(x, n/2)
        val2 = x if n & 1 else 1
        return val1 * val1 * val2
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if x == 0: return 0
        if n < 0: x = 1.0 / x
        return self._myPow(x, abs(n))