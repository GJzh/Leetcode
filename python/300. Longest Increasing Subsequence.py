class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i in range(len(nums)):
            low = 0
            high = len(dp) - 1
            while low <= high:
                mid = (low + high) // 2
                if (dp[mid] >= nums[i]):
                    high = mid-1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[i])
            else:
                dp[low] = nums[i]
        return len(dp)

