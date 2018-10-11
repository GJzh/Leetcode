class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        status = {}
        status[0] = 1
        cnt = 0
        s = 0
        for num in nums:
            s += num
            if s - k in status:
                cnt += status[s - k]
            if s not in status:
                status[s] = 1
            else:
                status[s] += 1
        return cnt