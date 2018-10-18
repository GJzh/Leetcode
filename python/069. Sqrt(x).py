class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 1, x
        while left <= right:
            mid = (left + right) / 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right