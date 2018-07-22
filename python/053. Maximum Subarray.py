Solution1: DP
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        res = -1*float('inf')
        for i in range(len(nums)):
            temp = max(nums[i], temp+nums[i])
            res = max(res, temp)
        return res

Solution2: Divide and conquer
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.res = -1*float('inf')
        self._maxSubArray(0, len(nums)-1)
        return self.res
    
    def _maxSubArray(self, left, right):
        if left > right: return -1*float('inf')
        nums = self.nums
        mid = (left+right)//2
        self._maxSubArray(left, mid-1)
        self._maxSubArray(mid+1, right)
        leftMax = rightMax = temp = 0
        for i in range(mid-1,left-1,-1):
            temp += nums[i]
            leftMax = max(leftMax, temp)
        temp = 0
        for i in range(mid+1,right+1):
            temp += nums[i]
            rightMax = max(rightMax, temp)
        self.res = max(self.res, nums[mid] + leftMax + rightMax)

