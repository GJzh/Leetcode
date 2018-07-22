# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def takeFirst(a): 
            return a.start
        n = len(intervals)
        if n == 0: return []
        intervals.sort(key=takeFirst)
        cur = Interval(-sys.maxsize, -sys.maxsize)
        res = []
        for interval in intervals:
            if interval.start > cur.end:
                res.append(cur)
                cur = interval
            else:
                cur.end = max(cur.end, interval.end)
        res.append(cur)
        return res[1:]

