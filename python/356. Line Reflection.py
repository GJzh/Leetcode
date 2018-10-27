time: O(nlogn) space: O(n)
class Solution(object):
    def checkSymmetry(self, xs):
        if len(xs) == 1: return True
        left, right = 0, len(xs)-1
        while left <= right:
            if xs[left+1] - xs[left] != xs[right] - xs[right-1]:
                return False
            left += 1
            right -= 1
        return True
    
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        status = {}
        for x, y in points:
            if y not in status:
                status[y] = set()
            status[y].add(x)
        reference = None
        for y, xs in status.items():
            xs = sorted(xs)
            n = len(xs)
            if not self.checkSymmetry(xs): return False
            if n & 1:
                mid = xs[n/2]
            else:
                mid = (xs[n/2-1] + xs[n/2]) / 2
            if reference == None: reference = mid
            elif reference != mid: return False
        return True