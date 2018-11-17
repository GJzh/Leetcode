class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)
        if n == 0: return 0
        cars = sorted(zip(position, speed))
        times = [1.0 * (target - position) / speed for position, speed in cars]
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: ans += 1
            else: times[-1] = lead
        ans += 1
        return ans