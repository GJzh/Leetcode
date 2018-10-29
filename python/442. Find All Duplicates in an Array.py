Time: O(n) Space: O(1)
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in range(len(nums)):
            if nums[i] == i+1 or nums[i] == 0: continue
            pos = nums[i]-1
            nums[i] = 0
            while nums[pos] != 0 and nums[pos] != pos + 1:
                temp = nums[pos]
                nums[pos] = pos + 1
                pos = temp - 1
            if nums[pos] == pos + 1:
                res.add(nums[pos])
            else:
                nums[pos] = pos + 1
        
        return list(res)