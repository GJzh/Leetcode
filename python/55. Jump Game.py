class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = {}
        length = len(nums)
        if length == 0: return False
        if length == 1: return True
        d = nums[0]
        k = 1
        while k <= d:
            d = max(d, k+nums[k])
            k += 1
            if d >= length-1: return True                        
        return False

