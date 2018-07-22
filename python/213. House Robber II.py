class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]
        dp1 = []
        dp2 = []
        dp1.append(nums[0])
        dp1.append(nums[0])
        dp2.append(0)
        dp2.append(nums[1])
        for i in range(2, length):
            dp1.append(max(dp1[i-2]+nums[i], dp1[i-1]))
            dp2.append(max(dp2[i-2]+nums[i], dp2[i-1]))
        return max(dp1[-2], dp2[-1])

