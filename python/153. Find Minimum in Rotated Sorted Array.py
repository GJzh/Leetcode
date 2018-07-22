class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        return self._findMin(0, len(nums)-1)
    
    def _findMin(self, start, end):
        if start == end: return self.nums[start]
        if (self.nums[start] < self.nums[end]): return self.nums[start]
        mid = (end+start)//2
        if self.nums[mid] > self.nums[end]:
            return self._findMin(mid+1, end)
        else:
            return self._findMin(start, mid)

