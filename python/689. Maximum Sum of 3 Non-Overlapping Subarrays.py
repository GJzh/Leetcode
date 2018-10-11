class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n
        dp3 = [0] * n
        status1 = [0] *n
        status2 = [None] * n
        status3 = (0, 0, 0)
        cur = 0
        maxSum = 0
        for i in range(k):
            cur += nums[i]
        dp1[k-1] = cur
        for i in range(k, n):
            cur += (nums[i] - nums[i-k])
            # update dp1
            if cur > dp1[i-1]:
                dp1[i] = cur
                status1[i] = i - k + 1
            else:
                dp1[i] = dp1[i-1]
                status1[i] = status1[i-1]
            # update dp2
            if i >= 2*k-1:
                if dp1[i-k] + cur > dp2[i-1]:
                    dp2[i] = dp1[i-k] + cur
                    status2[i] = (status1[i-k], i - k + 1)
                else:
                    dp2[i] = dp2[i-1]
                    status2[i] = status2[i-1]
            # update dp3
            if i >= 3*k-1:     
                if dp2[i-k] + cur > dp3[i-1]:
                    dp3[i] = dp2[i-k] + cur
                    status3 = (status2[i-k][0], status2[i-k][1], i - k  + 1)
                else:
                    dp3[i] = dp3[i-1]
        return status3