class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str)
        idx = 0
        while idx < length and str[idx] == ' ':
            idx += 1
        sign = 1
        if idx < length and (str[idx] == '+' or str[idx] == '-'):
            sign = 1 if str[idx] == '+' else -1
            idx += 1
        if not (idx < length and str[idx] >= '0' and str[idx] <= '9'): return 0
        num = 0
        while idx < length and str[idx] >= '0' and str[idx] <= '9':
            num = 10 * num + ord(str[idx]) - ord('0')
            idx += 1
        num *= sign
        num = num if num <= 2147483647 else 2147483647
        num = num if num >= -2147483648 else -2147483648
        return num

