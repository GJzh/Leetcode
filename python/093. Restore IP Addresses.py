class Solution(object):
    def isValid(self, t):
        if int(t) > 255: return False
        if len(t) > 1 and t[0] == '0': return False
        return True
        
    def dfs(self, s, idx, cur, res):
        if idx == len(s):
            if len(cur) == 4: res.append(".".join(cur))
            return
        if len(cur) >= 4: return
        t = ""
        for i in range(3):
            if idx+i >= len(s): break
            t += s[idx+i]
            if self.isValid(t):
                cur.append(t)
                self.dfs(s, idx+i+1, cur, res)
                cur.pop()
        return
        
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cur = []
        res = []
        self.dfs(s, 0, cur, res)
        return res