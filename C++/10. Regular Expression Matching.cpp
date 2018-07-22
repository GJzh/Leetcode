class Solution {
public:
    bool isMatch(string s, string p) 
    {
        int m = s.length();
        int n = p.length();
        vector<vector<bool>> dp = vector<vector<bool>>(m+1, vector<bool>(n+1, false));
        dp[0][0] = true;
        for(int j = 2; j <= n; j += 2)
        {
            dp[0][j] = (dp[0][j-2] && p[j-1] == '*');
        }
        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                char c1 = s[i-1];
                char c2 = p[j-1];
                if (c2 != '*' && c2 != '.')
                {
                    dp[i][j] = dp[i-1][j-1] && (c1 == c2);
                }
                else if (c2 == '.')
                {
                    dp[i][j] = dp[i-1][j-1];
                }
                else if (j > 1)
                {
                    if (dp[i][j-2] || dp[i][j-1])
                    {
                        dp[i][j] = true;
                    }
                    else if (dp[i-1][j] && (s[i-1] == p[j-2] || p[j-2] == '.') ) 
                    {
                        dp[i][j] = true;
                    }
                }
            }
        }
        return dp[m][n];
    }
};
