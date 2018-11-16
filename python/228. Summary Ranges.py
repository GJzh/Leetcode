class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        if n == 0: return []
        start, end = nums[0], nums[0]
        ans = []
        for i in range(1, n):
            if nums[i] == end + 1:
                end += 1
            else:
                cur = str(start) + "->" + str(end) if start != end else str(start)
                ans.append(cur)
                start = end = nums[i]
        cur = str(start) + "->" + str(end) if start != end else str(start)
        ans.append(cur)
        return ans