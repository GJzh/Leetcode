class Solution(object):
    class Ancestor():
        def __init__(self, n):
            self.v = [i for i in range(n)]
        
        def find(self, k):
            while k != self.v[k]:
                k = self.v[k]
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