class Solution(object):
    def getCondition(self, expression):
        condition = expression[self.idx]
        self.idx += 1
        return condition
    
    def getValue(self, expression):
        val = ""
        while self.idx < len(expression) and expression[self.idx].isdigit():
            val += expression[self.idx]
            self.idx += 1
        return val
    
    def _parseTernary(self, expression):
        if expression[self.idx].isdigit():
            return self.getValue(expression)
        condition = self.getCondition(expression)
        if self.idx == len(expression) or expression[self.idx] != '?': return condition
        self.idx += 1
        val1 = self._parseTernary(expression)
        self.idx += 1
        val2 = self._parseTernary(expression)
        if condition == 'T':
            return val1
        else:
            return val2
    
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        self.idx = 0
        return self._parseTernary(expression)