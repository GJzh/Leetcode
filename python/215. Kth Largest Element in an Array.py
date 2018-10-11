class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        time complexity: O(nlog(min(k, n-k+1)))
        """
        q = []
        n = len(nums)
        if k <= n / 2:
            for num in nums:
                if len(q) < k:
                    heapq.heappush(q, num)
                elif num > q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, num)
            return q[0]
        else:
            k = n - k + 1
            for num in nums:
                if len(q) < k:
                    heapq.heappush(q, -num)
                elif num < -q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, -num)
            return -q[0]