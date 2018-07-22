class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0: return True
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        if n == 0: return False
        if m * n < len(word): return False
        self.board = board
        self.word = word
        self.hash = {}
        for i in range(m):
            for j in range(n):
                if self._exist(i, j, 0): return True
        return False
    
    def _exist(self, i, j, idx):
        if self.word[idx] != self.board[i][j]: return False
        self.hash[(i,j)] = True
        if idx + 1 >= len(self.word): return True
        m = len(self.board)
        n = len(self.board[0])
        if i-1 >= 0 and (i-1,j) not in self.hash and self._exist(i-1, j, idx+1): return True
        if i+1 < m and (i+1,j) not in self.hash and self._exist(i+1, j, idx+1): return True
        if j-1 >= 0 and (i,j-1) not in self.hash and self._exist(i, j-1, idx+1): return True
        if j+1 < n and (i,j+1) not in self.hash and self._exist(i, j+1, idx+1): return True
        del(self.hash[(i,j)])
        return False

