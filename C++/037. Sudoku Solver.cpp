class Solution {
private:
    bool solveSudoku2(vector<vector<char>>& board, int row, int col)
    {
        int row2, col2;
        if (row==9){return true;}
        else if (col==8){row2=row+1; col2=0;}
        else {row2=row; col2=col+1;}
        if (board[row][col]!='.')
        {
            return isValid(board,row,col) && solveSudoku2(board,row2,col2);
        }
        for (int i=1;i<=9;i++)
        {
            board[row][col]='0'+i;
            if (isValid(board,row,col) && solveSudoku2(board,row2,col2)){return true;}
        }
        board[row][col]='.';
        return false;
    }
    bool isValid(vector<vector<char>>& board, int row, int col)
    {
        int val = board[row][col];
        if(val-'0'<1 || val-'0'>9){return false;}
        for (int i=0;i<9;i++)
        {
            if(val==board[i][col] && i!=row) return false;
            if(val==board[row][i] && i!=col) return false;
        }
        int row0 = row/3*3;
        int col0 = col/3*3;
        for (int i=row0;i<row0+3;i++)
        {
            for (int j=col0;j<col0+3;j++)
            {
                if(val==board[i][j] && !(i==row && j==col)) return false;
            }
        }
        return true;
    }
public:
    void solveSudoku(vector<vector<char>>& board) {
        if (board.size()!=9 || board[0].size()!=9){return;}
        solveSudoku2(board, 0, 0);
    }
};
