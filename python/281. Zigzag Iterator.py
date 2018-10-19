class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.x = 0
        self.y = 0
        self.v = [v1, v2]

    def next(self):
        """
        :rtype: int
        """
        val = self.v[self.x][self.y]
        self.x += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        n = len(self.v)
        start = self.x
        while self.x < n:
            if self.y < len(self.v[self.x]):
                return True
            self.x += 1
        self.y += 1
        self.x = 0
        while self.x < start:
            if self.y < len(self.v[self.x]):
                return True
            self.x += 1
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())