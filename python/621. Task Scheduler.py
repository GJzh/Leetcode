Solution 1:
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        output = [0]*26
        for i in tasks:
            output[ord(i)-ord('A')] += 1
 
        count = 0
        len_o = 0
        max_o = max(output)
        
        for i in output:
            if i==max_o:
                count = count+1
        print max_o, count   
        # case1: no idle -> res = len(tasks)
        # case2: idle -> res = (max_o-1)*(n+1)+count > len(tasks)
        # Note: if count >= n+1 -> no idle
        return max(len(tasks),(max_o-1)*(n+1)+count) 

Solution 2:
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        status = [0] * 26
        for task in tasks:
            status[ord(task) - ord('A')] += 1
        q = []
        for s in status:
            if s > 0: heapq.heappush(q, -1*s)
        res = 0
        print q
        while len(q) > 0:
            temp = []
            cnt = 0
            for i in range(n):
                if len(q) == 0: break
                temp.append(heapq.heappop(q)+1)
                cnt += 1
            for it in temp:
                if it < 0:
                    heapq.heappush(q, it)
            res += n if len(q) > 0 else cnt
        return res