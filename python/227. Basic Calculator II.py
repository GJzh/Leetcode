Solution 1
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        part1 = 0
        part2 = 0
        idx = 0
        while idx < n and s[idx] == " ":
            idx += 1
        val = ""
        while idx < n and s[idx].isdigit():
            val += s[idx]
            idx += 1
        part2 = int(val)
        
        while idx < n:
            # ignore white spaces
            while idx < n and s[idx] == " ":
                idx += 1
            if idx >= n: return part1 + part2
            # get the operator
            operator = s[idx]
            idx += 1
            # ignore white spaces
            while idx < n and s[idx] == " ":
                idx += 1
            # get the value
            val = ""
            while idx < n and s[idx].isdigit():
                val += s[idx]
                idx += 1
            val = int(val)
            # update part1 and part2
            if operator == "+":
                part1, part2 = part1 + part2, val
            elif operator == "-":
                part1, part2 = part1 + part2, -val
            elif operator == "*":
                part1, part2 = part1, part2 * val
            elif operator == "/":
                sign = 1 if part2 >= 0 else -1
                part1, part2 = part1, abs(part2) / val * sign
            else: return 0

        return part1 + part2

Solution 2:
class Solution(object):
    def _calculate(self, operands, operators):
        val1 = operands[-1]
        val2 = operands[-2]
        operands.pop()
        operands.pop()
        operator = operators[-1]
        operators.pop()
        if operator == "+":
            val = val1 + val2
        elif operator == "-":
            val = val1 - val2
        elif operator == "*":    
            val = val1 * val2
        elif operator == "/":    
            val = val1 / val2
        else:
            print("We do not support the operator " + operator)
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
            elif s[i] == "+" or s[i] == "-":
                while len(operators) and operators[-1] != "+" and operators[-1] != "-":
                    self._calculate(operands, operators)
                operators.append(s[i])
            elif s[i] == "*" or s[i] == "/":
                operators.append(s[i])
            else:
                pass
        while len(operators):
            self._calculate(operands, operators)
        return operands[0]