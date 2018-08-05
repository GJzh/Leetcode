# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        res = []
        n = len(intervals)
        pos = n
        for i in range(n):
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
            elif intervals[i].start > newInterval.end:
                pos = i
                break
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
        res.append(newInterval)
        for i in range(pos,n):
            res.append(intervals[i])
        return res
