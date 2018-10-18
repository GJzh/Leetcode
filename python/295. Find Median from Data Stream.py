class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smalls = []
        self.larges = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.smalls) == 0 or num < -self.smalls[0]:
            heapq.heappush(self.smalls, -num)
        else:
            heapq.heappush(self.larges, num)
        # check whether the sizes are balanced
        if len(self.smalls) - len(self.larges) >= 2:
            temp = -heapq.heappop(self.smalls)
            heapq.heappush(self.larges, temp)
        elif len(self.larges) - len(self.smalls) >= 2:
            temp = heapq.heappop(self.larges)
            heapq.heappush(self.smalls, -temp)
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smalls) == len(self.larges):
            return (-self.smalls[0] + self.larges[0]) / 2.0
        elif len(self.smalls) > len(self.larges):
            return -self.smalls[0]
        else:
            return self.larges[0]