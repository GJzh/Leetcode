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
