class Solution:
    def _search(self, nums, target, left, right):
        if left > right: return False
        if left == right: return nums[left] == target
        if nums[left] < nums[right]:
            if target < nums[left] or target > nums[right]:
                return False
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        else:
            return self._search(nums, target, left, mid-1) or self._search(nums, target, mid+1, right) 
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if not n: return False
        return self._search(nums, target, 0, len(nums)-1)
