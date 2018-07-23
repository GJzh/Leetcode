class Solution {
public:
    void dfs(vector<int>& nums, unordered_map<int,int>& hash, vector<int>& cur, vector<vector<int>>& res)
    {
        unordered_map<int, bool> hash2;
        if (cur.size() == nums.size())
        {
            res.push_back(cur);
            return;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (hash[nums[i]] > 0 && hash2[nums[i]] == false)
            {
                cur.push_back(nums[i]);
                hash[nums[i]]--;
                dfs(nums, hash, cur, res);
                cur.pop_back();
                hash[nums[i]]++;
                hash2[nums[i]] = true;
            }
        }
        return;
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        int n = nums.size();
        unordered_map<int, int> hash;
        vector<vector<int>> res = {};
        vector<int> cur = {};
        for (int i = 0; i < n; i++)
        {
            hash[nums[i]]++;
        }
        dfs(nums, hash, cur, res);
        return res;
    }
