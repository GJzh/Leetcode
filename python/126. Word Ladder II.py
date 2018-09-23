class Solution:
    def findNeighbours(self, word, nexts):
        for j in range(len(word)):
            c = word[j]
            for z in self.chars:
                if z == c: continue
                newWord = word[:j] + z + word[j+1:]
                if newWord not in self.words: continue
                if newWord not in self.visited or newWord in nexts:
                    if newWord not in self.parents: self.parents[newWord] = [] 
                    self.parents[newWord].append(word)
                if newWord not in self.visited:
                    self.visited[newWord] = True
                    nexts.append(newWord)
    
    def dfs(self, beginWord, endWord, cur, paths):
        if beginWord == endWord:
            cur.append(beginWord)
            paths.append(cur.copy())
            cur.pop()
            return
        cur.append(endWord)
        for parent in self.parents[endWord]:
            self.dfs(beginWord, parent, cur, paths)
        cur.pop()
        return
            
    
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.chars = []
        for i in range(26):
            self.chars.append(chr(ord('a') + i))
        self.parents = {}
        # list -> dict
        self.words = {}
        for word in wordList:
            self.words[word] = True
        # BFS
        cur = [beginWord]
        self.visited = {}
        self.visited[beginWord] = True
        status = False
        while len(cur)>0:
            nexts = []
            for word in cur:
                self.findNeighbours(word, nexts)
            cur = nexts
            if endWord in self.visited:
                status = True
                break
        # DFS finds all shortest transformation 
        res = []
        if status:
            cur = []
            paths = []
            self.dfs(beginWord, endWord, cur, paths)
            for path in paths:
                res.append(path[::-1])
        return res
