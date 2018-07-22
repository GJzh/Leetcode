class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        primes = [True] * (n+1)
        res = 0
        for i in range(2,n):
            if primes[i]:
                res += 1
                for j in range(i,n,i):
                    primes[j] = False
        return res

