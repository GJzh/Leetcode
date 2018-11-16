class Solution(object):
    def findCloestNumber(self, s):
        a, b = self.dictionary1[s[0]], self.dictionary1[s[1]]
        val = 16 * a + b
        ans = ""
        minDiff = float('inf')
        for k in range(-1, 2):
            c = a + k
            if c >= 0 and c < 16:
                diff = abs(c * 16 + c - val) 
                if diff < minDiff:
                    minDiff = diff
                    ans = self.dictionary2[c] * 2
        return ans
        
                
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        self.dictionary1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
        self.dictionary2 = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        ans = "#"
        for i in range(1, 7, 2):
            ans += self.findCloestNumber(color[i:i+2])
        return ans