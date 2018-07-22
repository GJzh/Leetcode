class Excel:

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.col = lambda c: ord(c) - ord('A')
        self.H, self.W = H, self.col(W) + 1
        self.values = collections.defaultdict(int)
        self.target = collections.defaultdict(lambda : collections.defaultdict(int))
        self.source = collections.defaultdict(lambda : collections.defaultdict(int))
        self.getIdx = lambda r, c: (r - 1) * self.W + self.col(c)

    def updateTgt(self, idx, delta):
        queue = [idx]
        while queue:
            first = queue.pop(0)
            for tgt in self.target[first]:
                self.values[tgt] += self.target[first][tgt] * delta
                queue.append(tgt)

    def removeSrc(self, idx):
        for src in self.source[idx]:
            del self.target[src][idx]
        del self.source[idx]

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        idx = self.getIdx(r, c)
        delta = v - self.values[idx]
        self.values[idx] = v
        self.removeSrc(idx)
        self.updateTgt(idx, delta)

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        return self.values[self.getIdx(r, c)]

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        idx = self.getIdx(r, c)
        self.removeSrc(idx)
        cval = self.values[idx]
        self.values[idx] = 0
        for src in strs:
            temp = src.split(':')
            for r in range(int(temp[0][1:]), int(temp[-1][1:]) + 1):
                for c in range(self.col(temp[0][0]), self.col(temp[-1][0]) + 1):
                    sidx = (r - 1) * self.W + c
                    self.target[sidx][idx] += 1
                    self.source[idx][sidx] += 1
                    self.values[idx] += self.values[sidx]
        self.updateTgt(idx, self.values[idx] - cval)
        return self.values[idx]

