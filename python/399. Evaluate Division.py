Solution 1 (DFS, O(e + e * q), e: the number of edge, q: the number of node):
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

Solution 2 (union find, O(e + q)):
class Solution(object):   
    def find(self, parents, variable):
        val = 1.0
        while parents[variable][0] != variable:
            val *= parents[variable][1]
            variable = parents[variable][0]
        return variable, val

    def merge(self, zeros, parents, variable1, variable2, val):
        if val == 0: 
            zeros[variable1] = True
            return
        if variable1 not in parents and variable2 not in parents:
            parents[variable1] = (variable2, val)
            parents[variable2] = (variable2, 1.0)
        elif variable1 not in parents:
            parents[variable1] = (variable2, val)
        elif variable2 not in parents:
            parents[variable2] = (variable1, 1.0 / val)
        else:
            var1, val1 = self.find(parents, variable1)
            var2, val2 = self.find(parents, variable2)
            parents[var1] = (var2, val * val2 / val1)
        return
            
    
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        zeros = {}
        parents = {}
        for i in range(len(equations)):
            variable1 = equations[i][0]
            variable2 = equations[i][1]
            val = values[i]
            self.merge(zeros, parents, variable1, variable2, val)
        ans = []
        for variable1, variable2 in queries:
            if variable1 in zeros: val = 0
            elif variable1 not in parents or variable2 not in parents: val = -1.0
            else:
                var1, val1 = self.find(parents, variable1)
                var2, val2 = self.find(parents, variable2)
                if var1 == var2:
                    val = 1.0 * val1 / val2
                else:
                    val = -1.0
            ans.append(val)
        return ans