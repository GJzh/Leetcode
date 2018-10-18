class Solution(object):
    def createPalindrome(self, half):
        res = 0
        temp = half
        cnt = 0
        while half > 0:
            res = 10 * res + half % 10
            half /= 10
            cnt += 1
        res = temp * (10 ** cnt) + res
        return res
    
    def checkDivision(self, upperbound, lowerbound, candidate):
        # check if candidate can be a multiplication of the two numbers between [lowerbound, upperbound]
        findPalindrome = False
        for i in range(upperbound, lowerbound-1, -1):
            if i * i < candidate: break
            if candidate % i == 0:
                findPalindrome = True
                break
        return findPalindrome
        
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        upperbound = 10 ** n - 1
        lowerbound = 10 ** (n-1)
        half = upperbound * upperbound / (10 ** n)
        findPalindrome = False
        while not findPalindrome:
            candidate = self.createPalindrome(half)
            findPalindrome = self.checkDivision(upperbound, lowerbound, candidate)
            half -= 1
        return candidate % 1337