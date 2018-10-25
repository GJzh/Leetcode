class Solution(object):
    def dfs(self, n, leftParentheses, cur, res):
        if len(cur) == 2 * n:
            res.append(copy.copy(cur))
            return
        # the number of "(" in cur is leftParentheses + (len(cur) - leftParentheses) / 2
        if leftParentheses + (len(cur) - leftParentheses) / 2 < n:
            cur += "("
            self.dfs(n, leftParentheses+1, cur, res)
            cur = cur[:len(cur)-1]
        if leftParentheses > 0:
            cur += ")"
            self.dfs(n, leftParentheses-1, cur, res)
            cur = cur[:len(cur)-1]
        return
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        cur = ""
        res = []
        self.dfs(n, 0, cur, res)
        return res