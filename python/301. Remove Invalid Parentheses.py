class Solution(object):
    def dfs(self, s, idx, leftPara, cnt1, cnt2, visited, cur, res):
        if (leftPara < 0 or cnt1 < 0 or cnt2 < 0): return
        if (idx == len(s)):
            if cnt1 == 0 and cnt2 == 0 and cur not in visited:
                visited[cur] = True
                res.append(cur)
            return
        if s[idx] == "(":
            # keep it
            cur += s[idx]
            self.dfs(s, idx+1, leftPara+1, cnt1, cnt2, visited, cur, res)
            cur = cur[:len(cur)-1]
            # remove it
            self.dfs(s, idx+1, leftPara, cnt1-1, cnt2, visited, cur, res)
        elif s[idx] == ")":
            # keep it
            cur += s[idx]
            self.dfs(s, idx+1, leftPara-1, cnt1, cnt2, visited, cur, res)
            cur = cur[:len(cur)-1]
            # remove it
            self.dfs(s, idx+1, leftPara, cnt1, cnt2-1, visited, cur, res)
        else:
            cur += s[idx]
            self.dfs(s, idx+1, leftPara, cnt1, cnt2, visited, cur, res)
        return
    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        stack = []
        cnt1 = 0
        cnt2 = 0
        for c in s:
            if (c == "("):
                cnt1 += 1
            elif (c == ")"):
                if cnt1 == 0:
                    cnt2 += 1
                else:
                    cnt1 -= 1
        cur = ""
        res = []
        visited = {}
        self.dfs(s, 0, 0, cnt1, cnt2, visited, cur, res)
        return res