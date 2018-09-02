class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [[0, 0] for i in range(n)]
        self.cols = [[0, 0] for i in range(n)]
        self.diagonals = [["-", 0] for i in range(2)]
        self.size = n
      
    def update(self, item, player):
        if item[0] == player:
            item[1] += 1
        else:
            item[0] = player
            item[1] = 1
        if item[1] == self.size:
            return player
        else:
            return 0
            
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
        if self.update(self.rows[row], player):
            return player
        
        if self.update(self.cols[col], player):
            return player
        if row == col and self.update(self.diagonals[0], player):
            return player
        if row + col == self.size-1 and self.update(self.diagonals[1], player):
            return player
        return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
