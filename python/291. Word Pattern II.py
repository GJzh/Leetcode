class Solution(object):
    def dfs(self, pattern, s, idx1, idx2):
        if idx1 == len(pattern) and idx2 == len(s): return True
        if idx1 >= len(pattern) or idx2 >= len(s): return False
        key = pattern[idx1]
        # key exists in self.vocabulary
        if key in self.patern2word:
            word = self.patern2word[key]
            if len(s) - idx2 >= len(word) and s[idx2:idx2+len(word)] == word:
                return self.dfs(pattern, s, idx1 + 1, idx2 + len(word))
            else:
                return False
        # key does not exist in self.vocabulary
        word = ""
        ans = False
        for i in range(idx2, len(s)):
            word += s[i]
            if word in self.word2pattern: continue
            self.patern2word[key] = word
            self.word2pattern[word] = key
            if self.dfs(pattern, s, idx1 + 1, i + 1): 
                ans = True
                break
            del self.patern2word[key]
            del self.word2pattern[word]
        return ans
            
    
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        self.patern2word = {}
        self.word2pattern = {}
        return self.dfs(pattern, str, 0, 0)