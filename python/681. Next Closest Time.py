class Solution(object):
    def findNext(self, digits, cur, upper):
        for digit in digits:
            if digit > upper: return '.'
            if digit > cur: return digit
        return '.'
    
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        '0', '1', or '2' must be in time becasue hh[0] <= '2'
        """
        digits = set()
        for i in range(len(time)):
            if time[i] != ":": digits.add(time[i])
        digits = list(digits)
        digits.sort()
        hh, mm = time.split(":")
        # change minutes
        m1 = self.findNext(digits, mm[1], '9')
        if m1 != '.': return (hh + ":" + mm[0] + m1)
        m0 = self.findNext(digits, mm[0], '5')
        if m0 != '.': return (hh + ":" + m0 + digits[0])
        # change hours
        mm = digits[0] + digits[0]
        if hh[0] < '2':
            h1 = self.findNext(digits, hh[1], '9')
        else:
            h1 = self.findNext(digits, hh[1], '3')
        if h1 != '.': return (hh[0] + h1 + ":" + mm)
        h0 = self.findNext(digits, hh[0], '2')
        if h0 != '.': return (h0 + digits[0] + ":" + mm)
        return digits[0] + digits[0] + ":" + digits[0] + digits[0]