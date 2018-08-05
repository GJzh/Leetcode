class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        n = len(nums)
        if not n: return
        for num in nums:
            if num != 0:
                nums[cnt] = num
                cnt += 1
        for i in range(cnt,n):
            nums[i] = 0
