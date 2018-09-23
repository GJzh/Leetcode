# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a%b)
    
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        cnt = 0
        for i in range(len(points)):
            slopes = {}
            dup = 1;
            for j in range(i+1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    dup += 1
                    continue
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y
                d = self.gcd(dx, dy)
                key = (dx/d, dy/d)
                if key in slopes:
                    slopes[key] += 1
                else:
                    slopes[key] = 1
            cnt = max(cnt, dup)
            for _, num in slopes.items():
                cnt = max(cnt, dup + num)
        return cnt
