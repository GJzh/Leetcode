class Solution(object):
    def dfs(self, s, words, idx, possible, cur, res):
        if idx == len(s):
            sentence = copy.copy(cur)
            res.append(sentence[:len(sentence)-1])
            return
        for i in range(idx, len(s)):
            if s[idx:i+1] in words and possible[i+1]:
                beforeChange = len(res)
                cur_size = len(cur)
                cur += (s[idx:i+1] + " ")
                self.dfs(s, words, i+1, possible, cur, res)
                cur = cur[:cur_size]
                if len(res) == beforeChange:
                    possible[i+1] = False
        
                
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        words = {}
        for word in wordDict:
            words[word] = True
        res = []
        cur = ""
        possible = [True] * (n+1)
        self.dfs(s, words, 0, possible, cur, res)
        return res