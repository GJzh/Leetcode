time: O(n), space: O(1)
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        n = len(nums)
        if n == 0:
            return [str(lower) + "->" + str(upper)] if lower != upper else [str(lower)]
        ans = []
        cur = lower
        nums.append(upper + 1)
        for num in nums:
            if num < cur: 
                continue
            elif num == cur:
                cur += 1
            else:
                a, b = cur, num - 1
                cur = num + 1
                missing = str(a) + "->" + str(b) if a != b else str(a)
                ans.append(missing) 
        return ans