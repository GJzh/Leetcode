class MyCalendarTwo(object):

    def __init__(self):
        self.intervals = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for overlap in self.overlaps:
            if min(end, overlap[1]) > max(start, overlap[0]):
                return False
        for interval in self.intervals:
            if min(end, interval[1]) > max(start, interval[0]):
                self.overlaps.append((max(start, interval[0]), min(end, interval[1])))
        self.intervals.append((start, end))
        return True