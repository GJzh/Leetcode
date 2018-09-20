class Solution(object):
    def _myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        res = x if n & 1 else 1
        temp = self._myPow(x, n/2)
        res *= (temp * temp)
        return res
        
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            sign = -1
        else:
            sign = 1
        n = abs(n)
        res = self._myPow(x, n)
        return res if sign == 1 else 1.0 / res
