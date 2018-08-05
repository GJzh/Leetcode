class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        power = 1
        y = x
        while y >= 10:
            y //= 10
            power *= 10
        while power :
            if x // power != x % 10:
                return False
            else:
                x = (x % power // 10)
                power //= 100
        return True
