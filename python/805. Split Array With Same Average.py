class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total = 0
        n = len(A)
        for num in A:
            total += num
        avg = total / n
        A.sort()
        candidates = []
        visited = {}
        for i in range(1,n // 2 + 1):
            val = avg * i
            if val - int(val) < 0.00001:
                candidates.append((i, int(avg * i)))
        for cnt, val in candidates:
            if self.dfs(A, 0, cnt, val, visited): return True
        return False
    
    def dfs(self, A, idx, cnt, target, visited):
        if (cnt, target) in visited and visited[(cnt, target)] <= idx: return False
        if cnt == 0 and target == 0: return True
        if cnt == 0 or idx == len(A) or target < A[idx]: return False
        if self.dfs(A, idx+1, cnt, target, visited): return True
        if self.dfs(A, idx+1, cnt-1, target - A[idx], visited): return True
        if (cnt, target) not in visited:
            visited[(cnt, target)] = idx
        else:
            visited[(cnt, target)] = min(visited[(cnt, target)], idx)

