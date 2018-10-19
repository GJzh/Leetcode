class Solution(object):
    def parse(self, A, flag):
        M = len(A)
        N = len(A[0])
        ans = {}
        if flag:
            for i in range(M):
                for j in range(N):
                    if A[i][j] == 0: continue
                    if j not in ans: ans[j] = []
                    ans[j].append((i, A[i][j]))
        else:
            for i in range(M):
                for j in range(N):
                    if A[i][j] == 0: continue
                    if i not in ans: ans[i] = []
                    ans[i].append((j, A[i][j]))
        return ans    
    
    def update(self, col, row, ans):
        for i, val1 in col:
            for j, val2 in row:
                ans[i][j] += val1 * val2
    
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(A)
        if M == 0: return []
        K = len(A[0])
        if K == 0: return []
        N = len(B[0])
        parseA = self.parse(A, True)
        parseB = self.parse(B, False)
        ans = [[0 for j in range(N)] for i in range(M)]
        for k in range(K):
            if k not in parseA or k not in parseB: continue
            self.update(parseA[k], parseB[k], ans)
        return ans