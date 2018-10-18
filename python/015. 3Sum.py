class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3: return []
        nums.sort()
        res = []
        i = 0
        while i <= n-3:
            left = i+1
            right = n-1
            num = nums[i]
            while left < right:
                if nums[left] + nums[right] < - num: left += 1
                elif nums[left] + nums[right] > - num: right -= 1
                else: 
                    res.append([num, nums[left], nums[right]])
                    a, b = nums[left], nums[right]
                    while left < right and nums[left] == a: left += 1
                    while left < right and nums[right] == b: right -= 1
            while i <= n-3 and nums[i] == num: i += 1
        return res

