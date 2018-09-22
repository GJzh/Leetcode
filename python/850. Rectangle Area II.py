Solution 1:
class Solution():
    def findWidth(self, actives):
        width = 0
        cur = 0
        actives.sort()
        for x1, x2 in actives:
            width += max(0, x2 - max(x1, cur))
            cur = max(cur, x2)
        return width
        
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        OPEN, CLOSE = True, False
        items = []
        for xmin, ymin, xmax, ymax in rectangles:
            items.append((ymin, OPEN, xmin, xmax))
            items.append((ymax, CLOSE, xmin, xmax))
        items.sort()
        cnt = 0
        cur = items[0][0]
        actives = []
        for y, status, x1, x2  in items:
            wdith = self.findWidth(actives)
            if status:
                actives.append((x1, x2))
            else:
                actives.remove((x1, x2))
            cnt += (y - cur) * wdith
            cur = y
        return cnt % 1000000007

Solution 2:
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.activeNum = 0
        self.total = 0
        self._left = None
        self._right = None
            
    @property    
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left
        
    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right
        
    def update(self, i, j, val):
        if i == j: return 0
        # val = 1 or -1
        if self.start == i and self.end == j:
            self.activeNum += val
        else:
            self.left.update(min(self.mid, i), min(self.mid, j), val)
            self.right.update(max(self.mid, i), max(self.mid, j), val)
        # the current range [self.start, self.end] is still covered
        if self.activeNum > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total
        return self.total

class Solution():      
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        ACTIVE = 1
        DEACTIVE = -1
        events = []
        global X
        X = set()
        for xmin, ymin, xmax, ymax in rectangles:
            X.add(xmin)
            X.add(xmax)
            events.append((ymin, xmin, xmax, ACTIVE))
            events.append((ymax, xmin, xmax, DEACTIVE))
        X = sorted(X)
        pos2id = {x:i for i, x in enumerate(X)}
        events.sort()
        segNode = Node(0, len(X)-1)
        cnt = 0
        width = 0
        prev_y = events[0][0]
        for y, x1, x2, val in events:
            cnt += (y - prev_y) * width
            width = segNode.update(pos2id[x1], pos2id[x2], val)
            prev_y = y
        
        return cnt % 1000000007
