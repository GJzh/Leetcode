class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        if (m * n) == 0: return ""
        idx1, idx2 = m-1, n-1
        carry = 0
        res = ""
        while idx1 >= 0 or idx2 >=0:
            val = carry
            if idx1 >= 0:
                val += int(num1[idx1])
                idx1 -= 1
            if idx2 >= 0:
                val += int(num2[idx2])    
                idx2 -= 1
            res += str(val % 10)
            carry = val / 10
        if carry > 0:
            res += str(carry)
        return res[::-1]