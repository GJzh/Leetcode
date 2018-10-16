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
    def upperBound(self, q, target):
        left, right = 0, len(q)-1
        while left <= right:
            mid = (left+right)/2
            if q[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
        
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        q = []
        for num in nums:
            pos = self.upperBound(q, num)
            if pos >= len(q):
                q.append(num)
            else:
                q[pos] = num
        return len(q)

