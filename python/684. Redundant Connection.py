from Queue import Queue
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        degree = [0] * (N + 1)
        neighbors = [[] for i in range(N+1)]
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
            neighbors[a].append(b)
            neighbors[b].append(a)
        cur = Queue()
        for k in range(N+1):
            if degree[k] == 1:
                cur.put(k)
        while cur.qsize() > 0:
            k = cur.get()
            for neighbor in neighbors[k]:
                if degree[neighbor] >= 2:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        cur.put(neighbor)
        for i in range(N-1, -1, -1):
            a, b = edges[i]
            if degree[a] > 1 and degree[b] > 1:
                return edges[i]