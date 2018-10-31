class Solution(object):
    def _calculate(self, operands, operators):
        val1, val2 = operands.pop(), operands.pop()
        operator = operators.pop()
        if operator == "+":
            val = val1 + val2
        else:
            val = val1 - val2
        operands.append(val)
        return
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        cur = ""
        operands = []
        operators = []
        for i in range(n-1, -1, -1):
            if s[i].isdigit():
                cur += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(cur[::-1]))
                    cur = ""
            elif s[i] == "+" or s[i] == "-" or s[i] == ")":
                operators.append(s[i])
            elif s[i] == "(":
                while len(operators) and operators[-1] != ')':
                    self._calculate(operands, operators)
                operators.pop()
            else:
                pass
        while len(operators):
            self._calculate(operands, operators)
        return operands[0]