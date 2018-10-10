class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # save the index of non-matching "("s
        stack = []
        # save the previous non-matching point
        last = -1
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        res = max(res, i - last)
                    else:
                        res = max(res, i - stack[-1])
        return res