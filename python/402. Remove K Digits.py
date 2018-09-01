class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        size = len(num)
        stack = ["0"]
        for x in num:
            while k > 0 and int(x) < int(stack[-1]):
                stack.pop()
                k -= 1
            stack.append(x)
        while k:
            stack.pop()
            k -= 1
        return str(int("".join(stack)))
