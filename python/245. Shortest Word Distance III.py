class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = float('inf')
        pos = {}
        pos[word1] = float('-inf')
        pos[word2] = float('-inf')
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                res = min(res, i-pos[word2])
                pos[word1] = i
            elif word == word2:
                res = min(res, i-pos[word1])
                pos[word2] = i
        return res