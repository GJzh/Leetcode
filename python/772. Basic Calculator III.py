class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operators = []
        operands = []
        operand = ""
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while len(operators) > 0 and (operators[-1] == '*' or operators[-1] == '/'):
                    self._calculate(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self._calculate(operands, operators)
                operators.pop()

        print(operands, operators)
        while len(operators) > 0:
            self._calculate(operands, operators)
        return operands[0]
            
    def _calculate(self, operands, operators):
        operand1, operand2 = operands.pop(), operands.pop()
        operator = operators.pop()
        if operator == '+':
            operands.append(operand1 + operand2)
        elif operator == '-':
            operands.append(operand1 - operand2)
        elif operator == '*':
            operands.append(operand1 * operand2)
        else:
            operands.append(operand1 // operand2)

