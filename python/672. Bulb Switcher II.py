class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n > 6: n = (n % 6 + 6)
        return len(self._flipLights(n, m))
    
    def _flipLights(self, n, m):
        status = set()
        if m == 0:
            cur = 0
            for i in range(n):
                cur <<= 1
                cur += 1
            status.add(cur)
            return status
        res = self._flipLights(n, m-1)
        if len(res) == 2**n: return res
        for cur in res:
            temp1 = self.operator1(cur, n)
            temp2 = self.operator2(cur, n)
            temp3 = self.operator3(cur, n)
            temp4 = self.operator4(cur, n)
            status.add(temp1)
            status.add(temp2)
            status.add(temp3)
            status.add(temp4)
        return status
    
    def operator1(self, cur, n):
        x = (1 << n) - 1
        return cur ^ x
            
            
    def operator2(self,cur, n):
        for i in range(0, n, 2):
            cur ^= (1 << i)
        return cur
    
    def operator3(self,cur, n):
        for i in range(1, n, 2):
            cur ^= (1 << i)
        return cur
    
    def operator4(self,cur, n):
        for i in range(0, n, 3):
            cur ^= (1 << i)
        return cur

# Solution 2:
class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m * n == 0: return 1
        if n == 1: return 2
        if n == 2: return 4 - (m % 2)
        if m == 1: return 4
        if m == 2: return 7
        return 8

