class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.status = {}
        for i in range(len(nums)):
            if nums[i] not in self.status:
                self.status[nums[i]] = []
            self.status[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        m = len(self.status[target])
        idx = random.randint(0, m-1)
        return self.status[target][idx]