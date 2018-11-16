class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for point1 in points:
            status = {}
            for point2 in points:
                dist = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
                if dist not in status:
                    status[dist] = 1
                else:
                    status[dist] += 1
            for dist, num in status.items():
                if num >= 2:
                    ans += num * (num - 1)
            del status
        return ans