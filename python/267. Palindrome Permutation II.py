class Solution(object):
    def dfs(self, length, freqs, cur, res):
        if len(cur) == length: 
            res.append(cur)
            return
        for i in range(len(freqs)):
            if freqs[i][1] < 2: continue
            freqs[i] = (freqs[i][0], freqs[i][1]-2)
            cur += freqs[i][0]
            self.dfs(length, freqs, cur, res)
            cur = cur[:len(cur)-1]
            freqs[i] = (freqs[i][0], freqs[i][1]+2)
        return
                
        
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n == 0: return []
        freqs = {}
        for c in s:
            if c not in freqs:
                freqs[c] = 1
            else:
                freqs[c] += 1
        cnt = 0  
        t = ""
        freqs = freqs.items()
        for c, freq in freqs:
            if freq % 2 == 1:
                cnt += 1
                t = c
        if cnt > 1: return []
        cur = ""
        res = []
        self.dfs(n/2, freqs, cur, res)
        for i in range(len(res)):
            if cnt == 0:
                res[i] = (res[i] + res[i][::-1])
            else:
                res[i] = (res[i] + t + res[i][::-1])
        return res