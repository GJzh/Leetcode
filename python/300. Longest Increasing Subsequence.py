Solution 1:
# O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        dp = [1] * n 
        res = 1
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                res = max(res, dp[i])
        return res
Solution 2:
# O(nlogn)
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

