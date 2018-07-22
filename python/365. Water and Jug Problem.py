class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        return x + y == z or x + y > z and z % self.gcd(x, y) == 0
    
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a%b)

