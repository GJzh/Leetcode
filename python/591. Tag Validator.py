class Solution:
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and len(stack) == 0: return False
            if code[i:i+9] == "<![CDATA[":
                j = i + 9
                i = code.find("]]>", j)
                if i == -1: return False
                i += 2
            elif code[i:i+2] == "</":
                if len(stack) == 0: return False
                j = i + 2
                i = code.find(">", j)
                if i == -1: return False
                tag = code[j:i]
                if stack[-1] == tag:
                    stack.pop()
                else:
                    return False
            elif code[i] == '<':
                j = i + 1
                i = code.find(">", j)
                if i < 0 or i - j < 1 or i - j > 9: return False
                for k in range(j, i):
                    if ord(code[k]) < ord('A') or ord(code[k]) > ord('Z'): return False
                tag = code[j:i]
                stack.append(tag)
            i += 1
        return len(stack) == 0

