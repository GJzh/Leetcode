class Solution(object):
    def _atMostNGivenDigitSet(self, D, N):
        length = len(str(N))
        digit = N / (10 ** (length - 1))
        residual = N % (10 ** (length - 1))
        ans = self.lowers[digit] * (len(D) ** (length - 1))
        if str(digit) in D:
            if length == 1:
                ans += 1
            elif len(str(residual)) == length - 1:
                ans += self._atMostNGivenDigitSet(D, residual)
        return ans
        
    
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        length = len(str(N))
        self.lowers = [0] * 10
        start = int(D[0]) + 1
        cnt = 1
        for i in range(1, len(D)):
            for j in range(start, int(D[i])+1):
                self.lowers[j] = cnt
            start = int(D[i])+1
            cnt += 1
        for j in range(start, 10):
            self.lowers[j] = cnt
        ans = 0
        for i in range(1, length):
            ans += len(D) ** i
        ans += self._atMostNGivenDigitSet(D, N)
        return ans