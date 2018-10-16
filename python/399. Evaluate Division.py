Solution 1 (DFS):
class Solution(object):
    def dfs(self, graph, visited, x, y):
        if x == y: return 1.0, True
        for z, val in graph[x].items():
            if z not in visited:
                visited[z] = True
                d, flag = self.dfs(graph, visited, z, y)
                del visited[z]
                if flag: return val * d, True
        return -1.0, False
    
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for i in range(len(equations)):
            x, y = equations[i]
            val = values[i]
            if x not in graph: graph[x] = {}
            if y not in graph: graph[y] = {}
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        
        res = []
        visited = {}
        for x, y in queries:
            if x not in graph or y not in graph: 
                res.append(-1.0)
            else:
                visited[x] = True
                ans, flag = self.dfs(graph, visited, x, y)
                if flag:
                    res.append(ans)
                else:
                    res.append(-1.0)
                del visited[x]
        return res

Solution 2 (union find):
class Solution(object):   
    def find(self, parents, k):
        val = 1.0
        while parents[k][0] != k:
            val *= parents[k][1]
            k = parents[k][0]
        return k, val
    
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        parents = {}
        for i in range(len(equations)):
            x, y = equations[i]
            val = values[i]
            if x not in parents and y not in parents: 
                parents[x] = (y, val)
                parents[y] = (y, 1.0)
            elif x not in parents:
                parents[x] = (y, val)
            elif y not in parents:
                parents[y] = (x, 1.0 / val)    
            else:
                k1, val1 = self.find(parents, x)
                k2, val2 = self.find(parents, y)
                parents[k1] = (k2, val * val2 / val1)
        res = []
        for x, y in queries:
            if x not in parents or y not in parents: 
                res.append(-1.0)
            else:
                k1, val1 = self.find(parents, x)
                k2, val2 = self.find(parents, y)
                if k1 == k2:
                    res.append(val1 / val2)
                else:
                    res.append(-1.0)
        return res