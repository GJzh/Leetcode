class Solution(object):
    def find(self, k):
        while k != self.group[self.words[k]]:
            temp = k
            k = self.group[self.words[self.group[self.words[k]]]]
            self.group[temp] = k
        return k
        
    def merge(self, k1, k2):
        k1 = self.find(k1)
        k2 = self.find(k2)
        if self.sz[k1] < self.sz[k2]:
            self.group[self.words[k1]] = k2
            self.sz[k2] += self.sz[k1]
        else:
            self.group[self.words[k2]] = k1
            self.sz[k1] += self.sz[k2]
    
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        self.group = {}
        self.words = []
        self.sz = []
        for word1, word2 in pairs:
            if word1 not in self.group: 
                self.group[word1] = len(self.words)
                self.words.append(word1)
                self.sz.append(1)
            if word2 not in self.group: 
                self.group[word2] = len(self.words)
                self.words.append(word2)
                self.sz.append(1)
            self.merge(self.group[word1], self.group[word2])
        for i in range(len(words1)):
            word1, word2 = words1[i], words2[i]
            if word1 == word2: continue
            elif word1 in self.group and word2 in self.group and self.find(self.group[word1]) == self.find(self.group[word2]):
                continue
            else:
                return False
        return True