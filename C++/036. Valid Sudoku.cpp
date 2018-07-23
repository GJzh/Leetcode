class Solution {
public:
    bool CheckSudoku(int x,int y,vector<vector<char>>& board) {
        for(int i=0;i<9;i++)
        {
            if(y!=i && board[x][y]==board[x][i] || x!=i && board[x][y]==board[i][y])
            return false;
        }
        
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                if(board[x][y]==board[x/3*3+i][y/3*3+j] && x!=x/3*3+i && y!=y/3*3+j){return false;}
            }
        }
        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if (board[i][j]=='.'){continue;}
                if (!CheckSudoku(i,j,board)){return false;}
            }
        }
        return true;
    }
};
