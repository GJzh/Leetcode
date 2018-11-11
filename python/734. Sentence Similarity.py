class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        similarWords = {}
        for word1, word2 in pairs:
            if word1 not in similarWords:
                similarWords[word1] = {}
            similarWords[word1][word2] = True
        for i in range(len(words1)):
            if words1[i] == words2[i]: continue
            elif words1[i] in similarWords and words2[i] in similarWords[words1[i]]:
                continue
            elif words2[i] in similarWords and words1[i] in similarWords[words2[i]]:
                continue
            else:
                return False
        return True