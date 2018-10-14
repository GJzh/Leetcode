class Solution(object):
    def findNeighbors(self, word):
        neighbors = []
        for i in range(len(word)):
            c = word[i]
            for z in self.chars:
                if z == c: continue
                newWord = word[:i] + z + word[i+1:]
                if newWord in self.words and newWord not in self.visited:
                    self.visited[newWord] = True
                    neighbors.append(newWord)
        return neighbors
                    
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # a -z
        self.chars = []
        for i in range(26):
            self.chars.append(chr(ord('a') + i))
        # list -> dict
        self.words = {}
        for word in wordList:
            self.words[word] = True
        
        # BFS
        q = [beginWord]
        cnt = 1
        self.visited = {}
        self.visited[beginWord] = True
        while len(q):
            cnt += 1
            temp = []
            for word in q:
                neighbors = self.findNeighbors(word)
                for neighbor in neighbors:
                    if neighbor == endWord: return cnt
                    temp.append(neighbor)
            q = temp
        return 0