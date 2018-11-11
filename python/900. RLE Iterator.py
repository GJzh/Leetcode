class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.idx = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.idx >= len(self.A):
            return -1
        while self.idx + 1 < len(self.A):
            if self.A[self.idx] >= n:
                self.A[self.idx] -= n
                return self.A[self.idx+1]
            else:
                n -= self.A[self.idx]
                self.idx += 2
        return -1