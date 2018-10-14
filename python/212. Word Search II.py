class Solution(object):
    class Node():
        def __init__(self):
            self.ch = [None] * 26
            self.word = ""
    def addWords(self, root, word):
        node = root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.ch[idx]:
                node.ch[idx] = self.Node()
            node = node.ch[idx]
        node.word = word
        
    def dfs(self, node, i, j, visited, res):
        idx = ord(self.board[i][j]) - ord('a')
        if not node.ch[idx]: return
        visited[(i,j)] = True
        node = node.ch[idx]
        if node.word != "": res.add(node.word)
        m = len(self.board)
        n = len(self.board[0])
        if i-1 >= 0 and (i-1,j) not in visited: self.dfs(node, i-1, j, visited, res)
        if i+1 < m and (i+1,j) not in visited: self.dfs(node, i+1, j, visited, res)
        if j-1 >= 0 and (i,j-1) not in visited: self.dfs(node, i, j-1, visited, res)
        if j+1 < n and (i,j+1) not in visited: self.dfs(node, i, j+1, visited, res)    
        del visited[(i,j)]
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        if not m: return []
        n = len(board[0])
        if not n: return []
        self.board = board
        root = self.Node()
        for word in words:
            self.addWords(root, word)
        res = set()
        visited = {}
        for i in range(m):
            for j in range(n):
                self.dfs(root, i, j, visited, res)
        return list(res)