class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        idx = 0
        while idx < n:
            if seats[idx] == 1:
                break
            idx += 1
        ans = idx
        prev = idx
        while idx < n:
            if seats[idx] == 1:
                ans = max(ans, (idx - prev) / 2)
                prev = idx
            idx += 1
        ans = max(ans, n - prev - 1)
        return ans