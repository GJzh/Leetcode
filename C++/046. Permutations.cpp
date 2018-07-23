class Solution {
    void searchPermute(vector<int>& nums, unordered_map<int,int> &hash, int count, vector<int> list, vector<vector<int>> &res)
    {
        if(count==0){res.push_back(list);return;}
        for(int i=0;i<nums.size();i++)
        {
            if(!hash[nums[i]])
            {
                list.push_back(nums[i]);
                hash[nums[i]]=1;
                searchPermute(nums, hash, count-1, list, res);
                hash[nums[i]]=0;
                list.pop_back();
            }
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> res={};
        unordered_map<int,int> hash;
        vector<int> list={};
        searchPermute(nums, hash, n, list, res);
        return res;
    }
};
