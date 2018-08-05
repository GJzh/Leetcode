class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        n = len(digits)
        for i in range(n-1,-1,-1):
            val = digits[i] + carry
            carry = val // 10
            digits[i] = val % 10
        res = []
        if carry > 0: res.append(carry)
        for digit in digits:
            res.append(digit)
        return res
