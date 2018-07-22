class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return -1
        self.target = target
        self.nums = nums
        return self._search(0, n-1)
    
    def _search(self, left, right):
        if left == right: 
            return left if self.nums[left] == self.target else -1
        mid = (left + right) // 2
        nums = self.nums
        target = self.target
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[left]:
            if target >= nums[left] and target < nums[mid]:
                return self._search(left,mid-1)
            else:
                return self._search(mid+1,right)
        elif nums[mid] < nums[left]:
            if target > nums[mid] and target <= nums[right]:
                return self._search(mid+1,right)
            else:
                return self._search(left,mid-1)
        else:
            return right if self.nums[right] == self.target else -1

