class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a)
        n = len(b)
        i, j = m-1, n-1
        carry = 0
        nums = ""
        while i >= 0 or j >= 0:
            val = carry
            if i >= 0:
                val += int(a[i])
            if j >= 0:
                val += int(b[j])
            nums += str(val%2)
            carry = val / 2
            i -= 1
            j -= 1
        if carry > 0:
            nums += str(carry)
        return nums[::-1]