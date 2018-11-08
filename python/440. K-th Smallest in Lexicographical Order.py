class Solution(object):    
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1
        while k > 1:
            step = 0
            first, last = cur, cur + 1
            while first <= n:
                step += min(n+1, last) - first
                first *= 10
                last *= 10
            if step < k:
                cur += 1
                k -= step
            else:
                cur *= 10
                k -= 1
        return cur