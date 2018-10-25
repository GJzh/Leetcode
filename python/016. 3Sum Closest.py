class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        left, right = 0, n-1
        d = float('inf')
        res = float('inf')
        for i in range(n-2):
            left, right = i + 1, n-1
            while left < right:
                val = nums[left] + nums[right] + nums[i]
                if abs(val - target) < d: 
                    res = val
                    d = abs(val - target)
                if val == target:
                    break
                elif val < target:
                    left += 1
                else:
                    right -= 1
        return res