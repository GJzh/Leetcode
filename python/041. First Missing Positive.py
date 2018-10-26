class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        the missing positive num should in [1, n+1]
        """
        n = len(nums)
        if n == 0: return 1
        for i in range(n):
            if nums[i] > 0 and nums[i] <= n and nums[i] != i+1:
                cur = nums[i]
                nums[i] = 0
                while cur > 0 and cur <= n:
                    temp = nums[cur-1]
                    nums[cur-1] = cur
                    if cur == temp: break
                    cur = temp
        res = n+1
        for i in range(n):
            if nums[i] != i+1:
                res = i+1
                break
        return res