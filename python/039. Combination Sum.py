class Solution(object):
    def dfs(self, candidates, target, idx, cur, res):
        if target == 0: 
            res.append(copy.copy(cur))
            return
        if idx >= len(candidates) or candidates[idx] > target: return
        for i in range(idx, len(candidates)):
            if candidates[i] <= target:
                cur.append(candidates[i])
                self.dfs(candidates, target-candidates[i], i, cur, res)
                cur.pop()
            else:
                break
        return
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0: return []
        candidates.sort()
        cur = []
        res = []
        self.dfs(candidates, target, 0, cur, res)
        return res