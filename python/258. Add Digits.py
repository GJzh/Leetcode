class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = num % 9
        return 9 if res == 0 and num != 0 else res

