class Solution(object):
    '''
    n = len(w)
    sums[i] = w[0] + w[1] +... + w[i-1]
    sums[n-1]
    randomNum ~ [1, sum[n-1]]
    binary search to find the first item such that sums[i] >= randomNum
    '''

    def __init__(self, w):
        """
        :type w: List[int]
        """
        n = len(w)
        if n == 0: return
        self.sums = [0] * n
        self.sums[0] = w[0]
        for i in range(1, len(w)):
            self.sums[i] = self.sums[i-1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        total = self.sums[-1]
        randomNum = random.randint(1, total)
        # binary search
        left, right = 0, len(self.sums)-1
        while left <= right:
            mid = (left+right)/2
            if self.sums[mid] >= randomNum:
                right = mid - 1
            else:
                left = mid + 1
        return left