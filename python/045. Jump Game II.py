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
        res = []
        for i in range(n-1):
            if i + nums[i] > nextEnd:
                nextEnd = i + nums[i]
                cur = i
            if i == end:
                if nextEnd == end: return -1
                res.append(cur)
                end  = nextEnd
                cnt += 1
        if nextEnd >= n-1: 
            # print out the path
            res.append(n-1)
            print res
            return cnt
        else: 
            return -1