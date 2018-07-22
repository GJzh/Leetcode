class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [['-' for i in range(n)] for j in range(n)]
        
    
    def count(self, pos, direction, player):
        n = len(self.grid)
        x = pos[0] + direction[0]
        y = pos[1] + direction[1]
        if x < 0 or x >= n or y < 0 or y >= n or self.grid[x][y] != player: return 0
        else: return 1 + self.count((x,y), direction, player)
    
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = len(self.grid)
        self.grid[row][col] = player
        cnt = 1
        cnt += self.count((row,col), (1,0), player) + self.count((row,col), (-1,0), player)
        if cnt == n: return player
        else: cnt = 1
        cnt += self.count((row,col), (0,1), player) + self.count((row,col), (0,-1), player)
        if cnt == n: return player
        else: cnt = 1
        if row != col and row+col != n-1: return 0
        cnt += self.count((row,col), (1,1), player) + self.count((row,col), (-1,-1), player)
        if cnt == n: return player
        else: cnt = 1
        cnt += self.count((row,col), (-1,1), player) + self.count((row,col), (1,-1), player)
        if cnt == n: return player
        else: return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

Solution 2: (support multiple users)
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [['-', 0] for j in range(n)]
        self.cols = [['-', 0] for j in range(n)]
        self.diagonals = [['-', 0] for i in range(2)]
    
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = len(self.rows)
        if self.rows[row][0] == player: self.rows[row][1] += 1
        else: self.rows[row] = [player, 1]
        if self.cols[col][0] == player: self.cols[col][1] += 1
        else: self.cols[col] = [player, 1]
        if self.rows[row][1] == n or self.cols[col][1] == n: return player
        if row == col:
            if self.diagonals[0][0] == player:
                self.diagonals[0][1] += 1
                if self.diagonals[0][1] == n: return player
            else:
                self.diagonals[0] = [player, 1]
        if row + col == n-1:
            if self.diagonals[1][0] == player:
                self.diagonals[1][1] += 1
                if self.diagonals[1][1] == n: return player
            else:
                self.diagonals[1] = [player, 1]
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

