class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        n = len(ages)
        ages.sort()
        pos = -1
        for i in range(n):
            if ages[i] >= 100:
                pos = i
                break
        print ages
        res = 0
        left, right = 0, 0
        while left < n:
            age = ages[left]
            cnt = 0
            while left+cnt < n and ages[left+cnt] == age:
                cnt += 1
            upperBound = 2 * age - 14
            while right < n and ages[right] < upperBound:
                right += 1
            if age <= 100:
                res += cnt * max(0, right - left - 1)
            else:
                res += cnt * max(0, right - max(pos, left+1) )
            left += cnt
        return res