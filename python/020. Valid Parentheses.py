class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paraMap = {')': '(', ']': '[', '}': '{'}
        q = [None]
        for c in s:
            if c in paraMap and q[-1] == paraMap[c]:
                q.pop()
            else:
                q.append(c)
        return len(q) == 1

