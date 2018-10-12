class Solution(object):
    def dfs(self, num, target, idx, part1, part2, cur, res):
        if idx == len(num):
            if part1 + part2 == target:
                res.append(cur)
            return
        m = len(cur)
        for i in range(idx, len(num)):
            val = int(num[idx:i+1])
            # "+"
            cur += ('+' + num[idx:i+1])
            self.dfs(num, target, i+1, part1+part2, val, cur, res)
            cur = cur[:m]
            # "-"
            cur += ('-' + num[idx:i+1])
            self.dfs(num, target, i+1, part1+part2, -val, cur, res)
            cur = cur[:m]
            # "*"
            cur += ('*' + num[idx:i+1])
            self.dfs(num, target, i+1, part1, part2 * val, cur, res)
            cur = cur[:m]
            if val == 0:
                break
        return
            
    
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        n = len(num)
        if n == 0: return []
        res = []
        for i in range(n):
            val = int(num[:i+1])
            cur = num[:i+1]
            self.dfs(num, target, i+1, 0, val, cur, res)
            if val == 0:
                break
        return res