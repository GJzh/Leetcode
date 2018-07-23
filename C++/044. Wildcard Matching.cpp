class Solution {
public:
    bool isMatch(string s, string p) 
    {
        int m = s.length();
        int n = p.length();
        int idxs = 0, idxp = 0, idMatch = 0, idStart = -1;
        while(idxs < m)
        {
            if(s[idxs] == p[idxp] || p[idxp] == '?')
            {
                idxs++;
                idxp++;
            }
            else if(p[idxp] == '*')
            {
                idMatch = idxs;
                idStart = idxp;
                idxp++;
            }
            else if (idStart != -1)
            {
                idMatch++;
                idxs = idMatch;
                idxp = idStart + 1;
            }
            else
            {
                return false;
            }
        }
        while(idxp < n && p[idxp] == '*'){idxp++;}
        return (idxp == n);
    }
};
