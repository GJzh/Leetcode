class Solution(object):
    def check(self, board, x, y):
        visited = {}
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] != "." and board[i][j] in visited: return False
                visited[board[i][j]] = True
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            visited = {}
            for j in range(9):
                if board[i][j] != "." and board[i][j] in visited: return False
                visited[board[i][j]] = True
        for j in range(9):
            visited = {}
            for i in range(9):
                if board[i][j] != "." and board[i][j] in visited: return False
                visited[board[i][j]] = True
        for i in range(3):
            for j in range(3):
                if not self.check(board, 3 * i, 3 * j):
                    return False
        return True