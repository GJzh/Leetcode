import queue
class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        sums = [0] * (n+1)
        sums[0] = 0
        res = n+1
        for i in range(1, n+1):
            sums[i] = sums[i-1] + A[i-1]
        dq = queue.deque([0])
        for end in range(1, n+1):
            while dq and sums[end] - sums[dq[0]] >= K:
                res = min(res, end - dq[0])
                dq.popleft()
            while dq and sums[end] < sums[dq[-1]]:
                dq.pop()
            dq.append(end)
        return res if res < n+1 else -1
