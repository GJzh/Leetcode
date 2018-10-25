class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        idx = 0
        for i in range(n):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx