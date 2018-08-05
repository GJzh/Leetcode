class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        n = len(nums)
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
            if counts[num] > n // 2:
                return num
        return -1
