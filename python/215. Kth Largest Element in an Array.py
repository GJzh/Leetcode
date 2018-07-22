class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        n = len(nums)
        for num in nums:
            if (len(q) < k):
                heapq.heappush(q, num)
            elif q[0] < num:
                heapq.heappop(q)
                heapq.heappush(q, num)
        return q[0]

