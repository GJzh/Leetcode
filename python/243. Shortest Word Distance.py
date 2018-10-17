class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        pos1: the position of the last word1 (by now)
        pos2: the position of the last word2 (by now)
        """
        res = float('inf')
        pos1 = float('-inf')
        pos2 = float('-inf')
        if word1 == word2: return 0
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                res = min(res, i-pos2)
                pos1 = i
            if word == word2:
                res = min(res, i-pos1)
                pos2 = i
        return res