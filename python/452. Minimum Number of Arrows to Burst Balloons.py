class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0: return 0
        def takeFirst(a):
            return a[0]
        points.sort(key = takeFirst)
        arrows = []
        arrows.append(points[0])
        for point in points:
            if point[0] <= arrows[-1][1]:
                arrows[-1][0] = max(arrows[-1][0], point[0])
                arrows[-1][1] = min(arrows[-1][1], point[1])
            else:
                arrows.append(point)
        return len(arrows)

