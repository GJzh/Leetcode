class Solution(object):
    class BIT():
        def __init__(self, n):
            self.bit = [0] * (n+1)
            
        def addNum(self, k):
            while k < len(self.bit):
                self.bit[k] += 1
                k += k & (-k)
            return
            
        def getSum(self, k):
            res = 0
            while k >= 1:
                res += self.bit[k]
                k -= k & (-k)
            return res
            
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return []
        v = copy.copy(nums)
        v.sort()
        # get ranks
        ranks = {}
        for i in range(n):
            if v[i] not in ranks:
                ranks[v[i]] = i+1
        res = [0] * n
        bit = self.BIT(n)
        bit.addNum(ranks[nums[n-1]])
        for i in range(n-2,-1,-1):
            if ranks[nums[i]] == 1:
                res[i] = 0
            else:
                res[i] = bit.getSum(ranks[nums[i]]-1)
            bit.addNum(ranks[nums[i]])
                
        return res