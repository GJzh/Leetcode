class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        ancestors = [0] * n
        if len(edges) != n-1: return False
        for i in range(n):
            ancestors[i] = i
        for i, j in edges:
            if i == j: return False
            while ancestors[i] != i:
                i = ancestors[i]
            while ancestors[j] != j:
                j = ancestors[j]
            if i != j:
                ancestors[j] = i
            else:
                return False
        return True