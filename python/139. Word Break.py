class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if not n: return False
        max_size = 0
        for word in wordDict:
            max_size = max(max_size, len(word))
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for k in range(i-1,-1,-1):
                if s[k:i] in wordDict and dp[k]:
                    dp[i] = True
                    break
                if (i-k) >= max_size: break
                    
        return dp[n]
        
