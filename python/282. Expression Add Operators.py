class Solution(object):
    def dfs(self, num, target, idx, val1, val2, expression, ans):
        if idx >= len(num):
            if val1 + val2 == target:
                ans.append(expression)
        for i in range(idx, len(num)):
            cur = num[idx:i+1]
            val = int(cur)
            self.dfs(num, target, i+1, val1+val2, val, expression + "+" + cur, ans)
            self.dfs(num, target, i+1, val1+val2, -val, expression + "-" + cur, ans)
            self.dfs(num, target, i+1, val1, val2 * val, expression + "*" + cur, ans)
            if val == 0: break
        return
        
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        n = len(num)
        if n == 0: return []
        val1 = 0
        ans = []
        for i in range(n):
            expression = num[:i+1]
            val2 = int(expression)
            self.dfs(num, target, i+1, val1, val2, expression, ans)
            if val2 == 0: break
        return ans