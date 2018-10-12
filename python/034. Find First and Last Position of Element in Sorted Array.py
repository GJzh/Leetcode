class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return [-1, -1]
        # find the first element nums[i] such taht nums[i] >= target
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left == n or nums[left] != target: return [-1, -1]
        a = left
        # find the last element nums[i] such taht nums[i] <= target
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return [a, right]