class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0: return []
        if length == 1: return [nums]
        res = []
        for i in range(length):
            for combine in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + combine)
        return res

