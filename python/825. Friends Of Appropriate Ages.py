class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        n = len(ages)
        if n == 0: return 0
        ages.sort()
        ans = 0
        pos = 0
        start = 0
        while pos < n:
            nextPos = pos
            while nextPos < n and ages[nextPos] == ages[pos]:
                nextPos += 1
            num = nextPos - pos
            lowerBound = 0.5 * ages[pos] + 7
            while start < n and ages[start] <= lowerBound:
                start += 1
            ans += max(0, (nextPos - start - 1) * num)
            pos = nextPos
        return ans