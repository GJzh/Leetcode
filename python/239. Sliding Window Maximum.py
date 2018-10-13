class Solution(object):
    def inQueue(self, q, num):
        while len(q):
            val = q.pop()
            if val >= num:
                q.append(val)
                break
        q.append(num)
    
    def outQueue(self, q, num):
        val = q.popleft()
        if val != num:
            q.appendleft(val)
        return
                
        
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return []
        if n < k: return []
        q = collections.deque()
        for i in range(k-1):
            self.inQueue(q, nums[i])
        res = []
        for i in range(k-1, n):
            self.inQueue(q, nums[i])
            val = q.popleft()
            res.append(val)
            q.appendleft(val)
            self.outQueue(q, nums[i-k+1])
        return res