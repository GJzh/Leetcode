class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        if (n == 0) return {};
        unordered_map<string, int> hash;
        vector<vector<string>> res;
        for (int i = 0; i < n; i++)
        {
            string str = strs[i];
            sort(str.begin(), str.end());
            if (hash.find(str) == hash.end())
            {
                vector<string> v;
                res.push_back(v);
                hash[str] = res.size()-1;
            }
            res[hash[str]].push_back(strs[i]);
        }
        return res;
    }
};
