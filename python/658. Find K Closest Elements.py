class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        heapq minimum will be on the top, (-abs(diff), -num)
        """
        q = []
        n = len(arr)
        if n == 0: return []
        for num in arr:
            if len(q) < k:
                heapq.heappush(q, (-abs(num-x), -num))
            else:
                top = heapq.heappop(q)
                if -top[0] > abs(num - x):
                    heapq.heappush(q, (-abs(num-x), -num))
                elif -top[0] == abs(num - x):
                    if -top[1] > num:
                        heapq.heappush(q, (-abs(num-x), -num))
                    else:
                        heapq.heappush(q, top)
                else:
                    heapq.heappush(q, top)
        q.sort(key = lambda z: -z[1])
        res = [-q[i][1] for i in range(len(q))]
        return res