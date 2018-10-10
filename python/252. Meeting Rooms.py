# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def takeFirst(self, interval):
        return interval.start
    
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = self.takeFirst)
        end = 0
        for interval in intervals:
            if interval.start < end:
                return False
            else:
                end = interval.end
        return True