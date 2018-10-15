class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return -1
        end, nextEnd = 0, 0
        cnt = 0
        for i in range(n-1):
            nextEnd = max(nextEnd, i + nums[i])
            if i == end:
                if nextEnd == end: return -1
                end  = nextEnd
                cnt += 1
        if nextEnd >= n-1: return cnt
        else: return -1