class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                return [left+1, right+1]
            elif val < target:
                left += 1
            else:
                right -= 1
        return []
