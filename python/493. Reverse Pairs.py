class Solution:
    def lowerBound(self, v, val):
        left = 0
        right = len(v)-1
        while left <= right:
            mid = (left + right) // 2
            if v[mid] < val:
                left = mid+1
            else:
                right = mid-1
        return right+1
        
    def getSum(self, bit, index):
        res = 0
        while index > 0:
            res += bit[index]
            index -= index & (-index)
        return res
            
    def update(self, bit, index):
        while index < len(bit):
            bit[index] += 1
            index += index & (-index)
        
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n: return 0
        v = nums.copy()
        v.sort()
        val2Id = {}
        for i in range(n):
            val2Id[v[i]] = i + 1
            
        res = 0
        bit = [0] * (n+1)
        for i in range(n-1,-1,-1):
            if nums[i] / 2 > v[0]:
                index = self.lowerBound(v, nums[i] / 2)
                res += self.getSum(bit, index)
            self.update(bit, val2Id[nums[i]])
        return res
