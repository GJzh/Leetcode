class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        radius = 0
        heaterId = 0
        for house in houses:
            while heaterId < len(heaters)-1 and abs(heaters[heaterId+1] - house) <= abs(heaters[heaterId] - house):
                heaterId += 1
            radius = max(radius, abs(heaters[heaterId] - house))
        return radius