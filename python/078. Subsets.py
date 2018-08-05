class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if not n: return [[]]
        num = nums[-1]
        items = self.subsets(nums[:n-1])
        m = len(items)
        for i in range(m):
            items.append(items[i] + [num])
        return items
