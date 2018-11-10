class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        ans = [0] * n
        # forward
        cur = 0
        prev = float('-inf')
        for i in range(n):
            if ratings[i] > prev:
                cur += 1
            else:
                cur = 1
            ans[i] = cur
            prev = ratings[i]
        prev = float('-inf')
        cur = 0
        for i in range(n-1,-1,-1):
            if ratings[i] > prev:
                cur += 1
            else:
                cur = 1
            ans[i] = max(ans[i], cur)
            prev = ratings[i]
        return sum(ans)