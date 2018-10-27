Solution 1 (find&merge) - time: O(nlogn)  space: O(n), n is the number of nodes
class Solution(object):
    class Ancestor():
        def __init__(self, n):
            self.v = [i for i in range(n)]
        
        def find(self, k):
            tenm = k
            while k != self.v[k]:
                k = self.v[k]
            self.v[temp] = k
            return k
        
        def merge(self, a, b):
            k1 = self.find(a)
            k2 = self.find(b)
            self.v[k1] = k2
            return 
    
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 0: return 0
        ancestor = self.Ancestor(n)
        for edge in edges:
            ancestor.merge(edge[0], edge[1])
        cnt = 0
        visited = {}
        for i in range(n):
            k = ancestor.find(i)
            if k not in visited:
                visited[k] = True
                cnt += 1
        return cnt

Solution 2 (BFS) - time: O(m) space: O(m), m is the number of edges
from Queue import Queue
class Solution(object):
    
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 0: return 0
        status = {}
        for edge in edges:
            if edge[0] not in status: status[edge[0]] = []
            if edge[1] not in status: status[edge[1]] = []    
            status[edge[0]].append(edge[1])
            status[edge[1]].append(edge[0])
        cnt = 0
        visited = [False] * n
        for i in range(n):
            if visited[i]: continue
            cnt += 1
            if i not in status: continue
            visited[i] = True
            q = Queue()
            q.put(i)
            while q.qsize():
                cur = q.get()
                for j in status[cur]:
                    if not visited[j]:
                        visited[j] = True
                        q.put(j)
        return cnt