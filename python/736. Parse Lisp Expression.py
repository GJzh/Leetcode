class Solution(object):
    def passSpace(self, expression):
        while self.pos < len(expression) and expression[self.pos] == " ":
            self.pos += 1
            
    def getToken(self, expression):
        token = ""
        self.passSpace(expression)
        while self.pos < len(expression) and expression[self.pos] != " " and expression[self.pos] != ")":
            token += expression[self.pos]
            self.pos += 1
        return token
        
    def getValue(self, variable):
        for i in range(len(self.scopes)-1, -1, -1):
            if variable in self.scopes[i]:
                return self.scopes[i][variable]
        return None
        
    def _evaluate(self, expression):
        self.scopes.append({})
        self.passSpace(expression)
        if self.pos == len(expression): return None
        if expression[self.pos] == '(': self.pos += 1
        
        token = self.getToken(expression)
        
        if token == "add":
            val1 = self._evaluate(expression)
            val2 = self._evaluate(expression)
            res = val1 + val2
        elif token == "mult":
            val1 = self._evaluate(expression)
            val2 = self._evaluate(expression)
            res = val1 * val2
        elif token == "let":
            while expression[self.pos] != ')':
                # expr in let expression
                self.passSpace(expression)
                if expression[self.pos] == "(":
                    self.pos += 1
                    res = self._evaluate(expression)
                    break
                    
                variable = self.getToken(expression)
                
                if expression[self.pos] == ")":
                
                    if variable[0].isalpha():
                        res = self.getValue(variable)
                    else:
                        res = int(variable)
                    break
                
                self.scopes[-1][variable] = self._evaluate(expression)
            
        elif token[0].isalpha():
            res = self.getValue(token)
        elif token[0].isdigit() or token[0] == '+' or token[0] == '-':
            res = int(token)
        else:
            res = None
        
        if self.pos < len(expression) and expression[self.pos] == ')': self.pos += 1
        self.scopes.pop()
        return res
        
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        self.scopes = []
        self.pos = 0
        return self._evaluate(expression)