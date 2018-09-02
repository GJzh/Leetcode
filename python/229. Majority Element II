class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        a, b = 0, 0
        ca, cb = 0, 0
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
            elif ca == 0:
                a = num
                ca = 1
            elif cb == 0:
                b = num
                cb = 1
            else:
                ca -= 1
                cb -= 1
        ca = 0
        cb = 0
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
        res = []
        if ca > len(nums) / 3:
            res.append(a)
        if cb > len(nums) / 3:
            res.append(b)
        return res
