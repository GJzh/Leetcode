class Solution(object):
    def dfs(self, board, idx):
        m = len(board)
        n = len(board[0])
        x, y = 0, 0
        while idx < 81:
            x = idx / 9
            y = idx % 9
            if board[x][y] == '.': break
            idx += 1
        if idx == 81: return True
        for i in range(1,10):
            if str(i) not in self.rows[x] and str(i) not in self.cols[y] and str(i) not in self.blocks[x/3][y/3]:
                self.rows[x][str(i)] = True
                self.cols[y][str(i)] = True
                self.blocks[x/3][y/3][str(i)] = True
                board[x][y] = str(i)
                if self.dfs(board, idx+1): return True
                board[x][y] = '.'
                del self.rows[x][str(i)]
                del self.cols[y][str(i)]
                del self.blocks[x/3][y/3][str(i)]
        return False
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.rows = [{} for i in range(9)]
        self.cols = [{} for i in range(9)]
        self.blocks = [[{} for j in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.': continue
                self.rows[i][val] = True
                self.cols[j][val] = True
                self.blocks[i/3][j/3][val] = True
        
        self.dfs(board, 0)
        return