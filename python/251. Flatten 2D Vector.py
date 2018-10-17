class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.x = 0
        self.y = 0

    def next(self):
        """
        :rtype: int
        """
        val = self.vec2d[self.x][self.y]
        self.y += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.x >= len(self.vec2d): return False
        if self.y == len(self.vec2d[self.x]):
            self.x += 1
            while self.x < len(self.vec2d) and len(self.vec2d[self.x]) == 0:
                self.x += 1
            if self.x == len(self.vec2d): return False
            else: self.y = 0
        return True