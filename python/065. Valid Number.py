class Solution:
    def isPositiveInteger(self, s, start, end):
        if start > end: return False
        return s[start:end+1].isdigit()
    
    def isInteger(self, s, start, end):
        if start > end: return False
        if s[start] == "+" or s[start] == "-":
            start += 1
        return self.isPositiveInteger(s, start, end)
    
    def isFloat(self, s, start, end):
        if start > end: return False
        if s[start] == "+" or s[start] == "-":
            start += 1
        if start > end: return False
        index = start
        while index <= end:
            if s[index] == ".":
                break
            index += 1
        if index == end+1:
            return self.isInteger(s, start, end)
        elif index == start:
            return self.isPositiveInteger(s, index+1, end)
        elif index == end:
            return self.isPositiveInteger(s, start, index-1)
        else:        
            return self.isPositiveInteger(s, start, index-1) and self.isPositiveInteger(s, index+1, end)
    
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start < end and s[start] == " ":
            start += 1
        while start < end and s[end] == " ":
            end -= 1   
        index = 0
        while index <= end:
            if s[index] == "e":
                break
            index += 1
        if index == end+1:
            return self.isFloat(s, start, end)
        else:
            return self.isFloat(s, start, index-1) and self.isInteger(s, index+1, end)
