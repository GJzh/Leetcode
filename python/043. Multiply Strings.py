class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        if m * n == 0: return ""
        if num1 == "0" or num2 == "0": return "0"
        res = ""
        carry = 0
        for k in range(n + m - 1):
            num = 0
            for i in range(max(0,k-n+1), min(m-1,k)+1):
                j = k - i
                num += int(num1[m-1-i]) * int(num2[n-1-j])
            res += str((num + carry) % 10)
            carry = (num + carry) / 10
        if carry > 0: res += str(carry)
        return res[::-1]