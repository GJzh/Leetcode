class Solution(object):
    def pos2grid(self, A):
        n = len(A)
        grid = []
        for i in range(n):
            cur = ""
            for j in range(n):
                if j == A[i]:
                    cur += "Q"
                else:
                    cur += "."
            grid.append(cur)
        return grid
    
    def dfs(self, n, i, cur, res):
        if i == n:
            res.append(self.pos2grid(cur))
            return
        for j in range(n):
            if self.vertical[j] and self.diagonal1[i+j] and self.diagonal2[i-j-1+n]:
                cur[i] = j
                self.vertical[j] = False
                self.diagonal1[i+j]  = False
                self.diagonal2[i-j-1+n] = False
                self.dfs(n, i+1, cur, res)
                cur[i] = -1
                self.vertical[j] = True
                self.diagonal1[i+j]  = True
                self.diagonal2[i-j-1+n] = True
        return
            
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        vertical[i]: [][i]
        diagonal1[k]: [i][j] such that i+j = k
        diagonal2[k]: [i][j] such that i-j = 1-n+k
        """
        self.vertical = [True] * n
        self.diagonal1 = [True] * (2*n-1)
        self.diagonal2 = [True] * (2*n-1)
        res = []
        cur = [-1] * n
        self.dfs(n, 0, cur, res)
        return res