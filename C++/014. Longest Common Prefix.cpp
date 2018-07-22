class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int size = strs.size();
        string result = "";
        if(size==0)
        {
            return result;
        }
        for(int j=0;j<strs[0].length();j++)
        {
            for(int i=0;i<size;i++)
            {
                if(strs[i][j]!=strs[0][j])
                {
                    return result;
                }
            }
            result += strs[0][j];
        }
        return result;
    }
};
