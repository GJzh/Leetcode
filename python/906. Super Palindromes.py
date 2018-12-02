class Solution(object):
    def isPalindrome(self, val):
        s = str(val)
        n = len(s)
        for i in range(n/2):
            if s[i] != s[n-1-i]:
                return False
        return True
            
    
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        L = long(L)
        R = long(R)
        cnt = 0
        for a0 in range(4):
            for a1 in range(4):
                for a2 in range(4):
                    for a3 in range(4):
                        for a4 in range(4):
                            s = str(a0) + str(a1) + str(a2) + str(a3) + str(a4)
                            num = long(s)
                            if num == 0: continue
                            s = str(num)
                            # even
                            if 2*a0*a0 + 2*a1*a1 + 2*a2*a2 + 2*a3*a3 + 2*a4*a4 < 10:
                                t = s + s[::-1]
                                val = long(t) ** 2
                                if val >= L and val <= R and self.isPalindrome(val):
                                    cnt += 1
                            # odd
                            if 2*a0*a0 + 2*a1*a1 + 2*a2*a2 + 2*a3*a3 + a4*a4 < 10:
                                t = s + s[::-1][1:]
                                val = long(t) ** 2
                                if val >= L and val <= R and self.isPalindrome(val):
                                    cnt += 1
        return cnt