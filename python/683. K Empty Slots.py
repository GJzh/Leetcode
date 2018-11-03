BIT  time: O(nlogn), space: O(n)
class Solution(object):
    class BIT():
        def __init__(self, n):
            self.bit = [0] * (n+1)
        
        def update(self, k):
            while k < len(self.bit):
                self.bit[k] += 1
                k += k & (-k)
                
        def getSum(self, k):
            ans = 0
            while k > 0:
                ans += self.bit[k]
                k -= k & (-k)
            return ans
    
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        if n == 0: return -1
        bloomings = {}
        p = self.BIT(n)
        for day in range(n):
            pos = flowers[day]
            bloomings[pos] = True
            p.update(pos)
            pos1 = pos - k - 1
            pos2 = pos + k + 1
            if pos1 >= 1 and pos1 in bloomings and p.getSum(pos-1) - p.getSum(pos1) == 0:
                return day + 1
            if pos2 <= n and pos2 in bloomings and p.getSum(pos2-1) - p.getSum(pos) == 0:
                return day + 1
        return -1    