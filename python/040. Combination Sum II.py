class Solution(object):
    def dfs(self, candidates, target, idx, cur, res):
        if target == 0: res.append(copy.copy(cur))
        if idx >= len(candidates): return
        while idx < len(candidates):
            val = candidates[idx]
            if val > target:
                break
            cur.append(val)
            self.dfs(candidates, target - val, idx + 1, cur, res)
            cur.pop()
            while idx < len(candidates) and candidates[idx] == val:
                idx += 1
        return
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        cur = []
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, cur, res)
        return res