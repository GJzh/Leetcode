class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0: sign = -1
        else: sign = 1
        res = 0
        x = abs(x)
        while x > 0:
            res = 10 * res + (x % 10)
            x //= 10
        res *= sign
        if res > (2 ** 31 - 1) or res < (-1 * 2 ** 31):
            return 0
        else:
            return res
