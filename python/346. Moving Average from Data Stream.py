class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = []
        self.size = size
        self.curSum = 0.0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        if len(self.nums) <= self.size:
            self.curSum += val
            return self.curSum / len(self.nums) 
        else:
            self.curSum += (val - self.nums[len(self.nums)-self.size-1])
            return self.curSum / self.size