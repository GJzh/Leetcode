class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        status = {}
        status[0] = -1
        sums = 0
        for i in range(n):
            sums += nums[i]
            residual = sums if k == 0 else sums % k
            if residual in status:
                if i - status[residual] >= 2: 
                    return True
            else:
                status[residual] = i
        return False