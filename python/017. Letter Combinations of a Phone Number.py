class Solution(object):
    def dfs(self, digits, idx, cur, res):
        if idx == len(digits):
            res.append(copy.copy(cur))
            return
        for c in self.status[int(digits[idx])]:
            cur += c
            self.dfs(digits, idx+1, cur, res)
            cur = cur[:len(cur)-1]
        return
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        self.status = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        cur = ""
        res = []
        self.dfs(digits, 0, cur, res)
        return res