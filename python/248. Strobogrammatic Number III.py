class Solution(object):
    def find(self, s, low, high):
        if len(s) > 0 and int(s) >= int(low) and int(s) <= int(high):
            if s[0] == '0' and len(s) > 1:
                pass
            else:
                self.res += 1
        if len(s) + 2 > len(high): return
        self.find("0" + s + "0", low, high)
        self.find("1" + s + "1", low, high)
        self.find("8" + s + "8", low, high)
        self.find("6" + s + "9", low, high)
        self.find("9" + s + "6", low, high)
    
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        corner case: 010, int("")
        """
        self.res = 0
        self.find('', low, high)
        self.find('0', low, high)
        self.find('1', low, high)
        self.find('8', low, high)
        return self.res