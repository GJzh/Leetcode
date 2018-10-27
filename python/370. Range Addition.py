class Solution(object):
    def increase(self, ans, start, end, cur):
        for i in range(start, end+1):
            ans[i] += cur
            
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        n = len(updates)
        ans = [0] * length
        if n == 0: return ans
        points = {}
        for update in updates:
            if update[0] not in points:
                points[update[0]] = update[2]
            else:
                points[update[0]] += update[2]
            if update[1] + 1 not in points:
                points[update[1] + 1] = -update[2]
            else:
                points[update[1] + 1] -= update[2]
        points = sorted(points.items())
        cur = 0
        start = 0
        i = 0
        for point in points:
            pos = point[0]
            end = pos - 1
            self.increase(ans, start, end, cur)
            cur += point[1]
            start = pos
        self.increase(ans, start, length-1, cur)
        return ans