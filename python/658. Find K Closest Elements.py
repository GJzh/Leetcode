Solution 1:
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        binary search: find the last num that <= x
        two pointers to search
        """
        n = len(arr)
        if n == 0: return []
        left, right = 0, n-1
        while left <= right:
            mid = (left + right)/2
            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1
        left, right = right, right+1
        res = []
        while left >= 0 and right < n and len(res) < k:
            if abs(arr[left] - x) < abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) == abs(arr[right] - x):
                if arr[left] < arr[right]: 
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            else:
                res.append(arr[right])
                right += 1
                    
        if len(res) < k:
            if left >= 0:
                while left >= 0 and len(res) < k: 
                    res.append(arr[left])
                    left -= 1
            else:
                while right < n and len(res) < k: 
                    res.append(arr[right])
                    right += 1
        res.sort()
        return res

Solution 2:
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