Solution 1:
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

Solution 2:
class Solution(object):
    def dfs(self, low, high, n, cur):
        if n == 0:
            if int(cur) >= low and int(cur) <= high:
                self.ans += 1
            return
        if n & 1:
            for single in self.singles:
                self.dfs(low, high, n-1, single)
        else:
            start = 1 if n == 2 else 0
            for i in range(start, len(self.doubles)):
                self.dfs(low, high, n-2, self.doubles[i][0] + cur + self.doubles[i][1])
        return
        
    
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        corner case: 010, int("")
        """
        self.singles = ["0", "1", "8"]
        self.doubles = [["0", "0"], ["1", "1"], ["8", "8"], ["6", "9"], ["9", "6"]]
        n1 = len(low)
        n2 = len(high)
        self.ans = 0
        for i in range(n1, n2+1):
            self.dfs(int(low), int(high), i, "")
        return self.ans