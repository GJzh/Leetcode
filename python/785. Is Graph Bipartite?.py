from Queue import Queue
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        if n == 0: return False
        colors = [0] * n
        for i in range(n):
            # already colored
            if colors[i] != 0: continue
            # i is the root of a tree
            # tranverse the tree with root i
            q = Queue()
            q.put(i)
            colors[i] = 1
            while q.qsize() > 0:
                cur = q.get()
                for node in graph[cur]:
                    if colors[node] == 0:
                        colors[node] = -colors[cur]
                        q.put(node)
                    else:
                        if colors[node] == colors[cur]:
                            return False
        return True