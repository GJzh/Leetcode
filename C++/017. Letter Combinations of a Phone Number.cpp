class Solution {
public:
    vector<string> letters;
    Solution()
    {
       letters = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    }
    
    vector<string> letterCombinations(string digits) 
    {
        int n = digits.length();
        if (n == 0) return {};
        int num =  digits.back() - '0';
        digits.pop_back();
        vector<string> prev = letterCombinations(digits);
        vector<string> res = {};
        if (prev.size() == 0)
        {
            prev = {""};
        }
        for(int i = 0; i < prev.size(); i++)
        {
            for (int j = 0; j < letters[num-2].size(); j++)
            {
                res.push_back(prev[i] + letters[num-2][j]);
            }
        }
            
        return res;
    }
};
