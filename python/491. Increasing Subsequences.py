class Solution(object):
    def dfs(self, nums, idx, cur, res):
        if idx >= len(nums): return
        visited = {}
        for i in range(idx, len(nums)):
            if nums[i] >= cur[-1] and nums[i] not in visited:
                visited[nums[i]] = True
                cur.append(nums[i])
                res.append(copy.copy(cur))
                self.dfs(nums, i+1, cur, res)
                cur.pop()
        return
                
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        in each round, if there exists reptated values, we can only use one of them
        to avoid missing possible paths, we should use the first-comming one
        """
        n = len(nums)
        if n == 0: return []
        res = []
        cur = []
        visited = {}
        for i in range(n-1):
            if nums[i] not in visited:
                visited[nums[i]] = True
                cur = [nums[i]]
                self.dfs(nums, i+1, cur, res)
        return res