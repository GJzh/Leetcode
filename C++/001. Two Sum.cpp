class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        if (n < 2) return {};
        unordered_map<int, int> hash;
        for (int i = 0; i < n; i++)
        {
            if (hash.count(target - nums[i]) > 0)
            {
                return {hash[target - nums[i]], i};
            }
            else
            {
                hash[nums[i]] = i;
            }
        }
        return {};
    }
};
