class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = []
        operators = {"+": True, "-": True, "*": True, "/": True}
        for token in tokens:
            if token not in operators:
                operands.append(int(token))
            else:
                operator = token
                operand2 = operands.pop()
                operand1 = operands.pop()
                if operator == "+":
                    operands.append(operand1 + operand2)
                elif operator == "-":
                    operands.append(operand1 - operand2)
                elif operator == "*":
                    operands.append(operand1 * operand2)
                else:
                    sign = 1 if operand1 * operand2 >= 0 else -1
                    operands.append(abs(operand1) / abs(operand2) * sign)
        return operands[0]