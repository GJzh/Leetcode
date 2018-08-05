class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        status = {}
        left, right = 0, 0
        res = 0
        for num in nums:
            if num not in status:
                if num-1 in status:
                    left = status[num-1]
                else:
                    left = 0
                if num+1 in status:
                    right = status[num+1]
                else:
                    right = 0
                val = 1 + left + right
                status[num] = val
                status[num-left] = val
                status[num+right] = val
                res = max(res, val)
        return res
