priority queue, time: O(logN), space: O(N)
class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.students = {}
        self.seats = {}
        self.intervals = []
        heapq.heappush(self.intervals, (-(N-1), -1, N))
        self.students[-1] = [-2,N]
        self.students[N] = [-1, N+1]
        self.N = N

    def seat(self):
        """
        :rtype: int
        """
        while len(self.intervals):
            negDist, start, end = self.intervals[0]
            if start in self.students and end in self.students and self.students[start][1] == end:
                break
            else:
                heapq.heappop(self.intervals)
        negDist, start, end = self.intervals[0]
        heapq.heappop(self.intervals)
        if start == -1:
            pos = 0
            if end == self.N: dist = end-pos-1
            else: dist = (end-pos)/2
            heapq.heappush(self.intervals, (-dist, pos, end))
        elif end == self.N:
            pos = self.N-1
            heapq.heappush(self.intervals, (-((pos-start)/2), start, pos))
        else:
            pos = (end + start) / 2
            heapq.heappush(self.intervals, (-((pos-start)/2), start, pos))
            heapq.heappush(self.intervals, (-((end-pos)/2), pos, end))
        self.students[pos] = [start, end]
        self.students[start][1] = pos
        self.students[end][0] = pos
        return pos

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        a, b = self.students[p]
        del self.students[p]
        self.students[a][1] = b
        self.students[b][0] = a
        if a == -1 or b == self.N: dist = b-a-1
        else: dist = (b-a)/2
        heapq.heappush(self.intervals, (-dist, a, b))
            


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)