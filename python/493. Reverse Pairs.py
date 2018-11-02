class Solution(object):
    class BIT():
        def __init__(self, n):
            self.v = [0] * (n+1)
        
        def getSum(self, k):
            ans = 0
            while k > 0:
                ans += self.v[k]
                k -= (k & -k)
            return ans
        
        def update(self, k):
            while k < len(self.v):
                self.v[k] += 1
                k += (k & -k)
    
    def lowerBound(self, v, target):
        left, right = 0, len(v)-1
        while left <= right:
            mid = (left + right) / 2
            if v[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return v[right]
    
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        v = copy.copy(nums)
        v.sort()
        ranks = {}
        for i in range(n):
            ranks[v[i]] = i + 1
        bit = self.BIT(n)
        ans = 0
        for i in range(n-1, -1, -1):
            target = nums[i] / 2.0
            if target > v[0]:
                num = self.lowerBound(v, target)
                rank = ranks[num]
                ans += bit.getSum(rank)
            bit.update(ranks[nums[i]])
        return ans
