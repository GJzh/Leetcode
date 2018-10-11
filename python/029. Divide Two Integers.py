class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        val1 = dividend if dividend >= 0 else -dividend
        val2 = divisor if divisor >= 0 else -divisor
        if val1 < val2: return 0
        temp1, temp2 = val1, val2
        c = 1
        res = 0
        while temp2 <= val1:
            temp2 <<= 1
            c <<= 1
        while temp1 >= val2:
            while temp1 >= temp2:
                temp1 -= temp2
                res += c
            temp2 >>= 1
            c >>= 1
        
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            res = -res
        if res < - 2 ** 31 or res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else: return res