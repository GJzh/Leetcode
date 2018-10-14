class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        k < left -> nums[k] = 0
        left <= k < mid -> nums[k] = 1
        k > right -> nums[k] = 2
        mid <= k <= right -> nums[k] unknown
        """
        n = len(nums)
        if not n: return
        left, mid, right = 0, 0, n-1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
            else:
                mid += 1

