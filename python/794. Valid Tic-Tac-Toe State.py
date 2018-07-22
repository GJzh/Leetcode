class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        rows = [0] * 3
        cols = [0] * 3
        diagonals = [0] * 2
        cnt1 = cnt2 = 0
        h = {'X': 1, 'O': -1, ' ': 0}
        for i in range(3):
            for j in range(3):
                c = board[i][j]
                rows[i] += h[c]
                cols[j] += h[c]
                if i == j: diagonals[0] += h[c]
                if i + j == 2: diagonals[1] += h[c]
                if c == 'X': cnt1 += 1
                if c == 'O': cnt2 += 1
        win1 = win2 = False     
        for x in rows:
            if x == 3: win1 = True
            elif x == -3: win2 = True
        for x in cols:
            if x == 3: win1 = True
            elif x == -3: win2 = True
        for x in diagonals:
            if x == 3: win1 = True
            elif x == -3: win2 = True
        if win1: return not win2 and cnt1 == cnt2 +1
        elif win2: return not win1 and cnt1 == cnt2
        else: return cnt1 == cnt2 + 1 or cnt1 == cnt2

