class Solution(object):
    def dfs(self, nums, idx, cur, ans):
        visited = {}
        while idx < len(nums):
            val = nums[idx]
            if val >= cur[-1] and val not in visited:
                visited[val] = True
                cur.append(val)
                if len(cur) >= 3: ans.append(cur[1:])
                self.dfs(nums, idx + 1, cur, ans)
                cur.pop()
            idx += 1
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
        cur = [float('-inf')]
        ans = []
        self.dfs(nums, 0, cur, ans)
        return ans