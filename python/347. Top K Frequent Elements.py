from collections import defaultdict
class Solution(object):
    def buttomKFrequent(self, nums, k):
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        q = []
        ans = []
        for num, cnt in freq.items():
            if len(q) < k or cnt < -q[0][0]:
                ans.append(q[0][1])
                heapq.heappop(q)
                heapq.heappush(q, (-cnt, num))
            ans.append(num)
        return ans
        
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == k: return nums
        if k > n / 2:
            return self.buttomKFrequent(nums, n - k)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        q = []
        for num, cnt in freq.items():
            if len(q) < k or cnt > q[0][0]:
                heapq.heappush(q, (cnt, num))
            if len(q) > k:
                heapq.heappop(q)
        ans = []
        while len(q):
            ans.append(heapq.heappop(q)[1])
        return ans