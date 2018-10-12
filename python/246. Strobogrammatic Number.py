class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        status = {"0": "0", "1": "1", "8": "8", "6":"9", "9": "6"}
        n = len(num)
        if n < 2: return True
        left, right = 0, n-1
        while left < right:
            if num[left] not in status or num[right] not in status or status[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True