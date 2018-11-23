class Solution(object):
    def order2str(self, A, order, overlaps):
        ans = [A[order[0]]]
        for idx in range(1, len(order)):
            i = order[idx-1]
            j = order[idx]
            ans.append(A[j][overlaps[i][j]:])
        return "".join(ans)
    
    def dfs(self, A, overlaps, visited, state, idx):
        if (state, idx) in visited: return
        n = len(A)
        cnt = -1
        for i in range(n):
            if (state >> i) & 1: continue
            nextState = state | (1 << i)
            self.dfs(A, overlaps, visited, nextState, i)
            if visited[(nextState,i)][0] + overlaps[idx][i] > cnt:
                cnt = visited[(nextState,i)][0] + overlaps[idx][i]
                order = [i] + visited[(nextState,i)][1]
            
        visited[(state, idx)] = (cnt, order)
        return
    
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        n = len(A)
        overlaps = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                for k in range(min(len(A[i]), len(A[j])), -1, -1):
                    if A[i].endswith(A[j][:k]):
                        overlaps[i][j] = k
                        break
        visited = {}
        finalState = 2 ** n - 1
        for i in range(n):
            visited[(finalState,i)] = (0, [])
        total = -1
        for i in range(n):
            state = 1 << i
            self.dfs(A, overlaps, visited, state, i)
            if visited[(state, i)][0] > total:
                total, order = visited[(state, i)]
                order = [i] + order
                ans = self.order2str(A, order, overlaps)
        return ans