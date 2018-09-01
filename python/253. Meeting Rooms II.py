# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        def takeFirst(interval):
            return interval.start
        intervals.sort(key = takeFirst)
        ends = []
        for interval in intervals:
            i = 0
            while i < len(ends):
                if interval.start >= ends[i]:
                    ends[i] = interval.end
                    break
                i += 1
            if i == len(ends):
                ends.append(interval.end)
        return len(ends)
