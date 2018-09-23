class Solution:    
    def generatePalindromic(self, prefix, odd):
        n = len(prefix)
        suffix = prefix[::-1]
        if odd:
            return int(prefix + suffix[1:])
        else:
            return int(prefix + suffix)
    
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        diff = num
        nearest = num
        candidates = []
        candidates.append(pow(10, len(n)) + 1)
        candidates.append(pow(10, len(n)-1) - 1)
        odd = len(n) % 2
        mid = (len(n) - 1) // 2
        prefix = int(n[:mid+1])
        for i in range(-1,2):
            candidates.append(self.generatePalindromic(str(prefix+i), odd))
        for candidate in candidates:
            if candidate == num: continue
            if abs(candidate - num) < diff:
                diff = abs(candidate - num)
                nearest = candidate
            elif abs(candidate - num) == diff:
                nearest = min(nearest, candidate)
        return str(nearest)
