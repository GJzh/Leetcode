class Solution:
    class Node:
        def __init__(self):
            self.str = ""
            self.ch = []
            for i in range(26):
                self.ch.append(None)
    
    def insertWord(self, node, word):
        #print(type(word), type(word[0]))
        for c in word:
            if node.ch[ord(c)-ord('a')] == None:
                node.ch[ord(c)-ord('a')] = self.Node()
            node = node.ch[ord(c)-ord('a')]
        node.str = word
                
    def dfs(self, node, i, j):
        idx = ord(self.board[i][j])-ord('a')
        if not node.ch[idx]: return
        self.hash[(i,j)] = True
        node = node.ch[idx]
        if node.str != "": 
            self.res.append(node.str)
            node.str = ""
        m = len(self.board)
        n = len(self.board[0])
        if i-1>=0 and (i-1,j) not in self.hash: self.dfs(node, i-1, j)
        if i+1<m and (i+1,j) not in self.hash: self.dfs(node, i+1, j)
        if j-1>=0 and (i,j-1) not in self.hash: self.dfs(node, i, j-1)
        if j+1<n and (i,j+1) not in self.hash: self.dfs(node, i, j+1)
        del(self.hash[(i,j)])
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = self.Node()
        for word in words:
            self.insertWord(root, word)
        self.res = []
        self.hash = {}
        self.board = board
        m = len(board)
        if m == 0: return []
        n = len(board[0])
        if n == 0: return []
        for i in range(m):
            for j in range(n):
                self.dfs(root, i, j)
        return self.res

