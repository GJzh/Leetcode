class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.nums = [0] * (n + 1)
        self.bit = [0] * (n + 1)
        for i in range(n):
            self.update(i, nums[i])
        return

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        k = i + 1
        while k < len(self.nums):
            self.bit[k] += diff
            k += k & (-k)
        return

    def getSum(self, k):
        k += 1
        cnt = 0
        while k > 0:
            cnt += self.bit[k]
            k -= k & (-k)
        return cnt
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j) - self.getSum(i-1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)