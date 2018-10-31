class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        else:
            sign = 1
        dividend, divisor = abs(dividend), abs(divisor)
        val1, val2 = dividend, divisor
        base = 1
        while val2 < val1:
            val2 <<= 1
            base <<= 1
        while val2 >= divisor:
            if val1 >= val2:
                ans += base
                val1 -= val2
            val2 >>= 1
            base >>= 1
        ans *= sign
        lowerBound = - 2 ** 31
        upperBound = 2 ** 31 -1
        if ans < lowerBound or ans > upperBound:
            return upperBound
        else:
            return ans