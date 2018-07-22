class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) 
    {
        int n = nums.size();
        if ( n < 3) return {};
        vector<vector<int>> res = {};
        sort(nums.begin(), nums.end());
        int i = 0;
        while(i < n-2)
        {
            int left = i + 1;
            int right = n - 1;
            while(left < right)
            {
                if (nums[left] + nums[right] < -1*nums[i])
                {
                    left++;
                }
                else if (nums[left] + nums[right] > -1*nums[i])
                {
                    right--;
                }
                else
                {
                    res.push_back({nums[i], nums[left], nums[right]});
                    int a = nums[left];
                    int b = nums[right];
                    while(left < right && nums[left] == a){left++;}
                    while(right > left && nums[right] == b){right--;}
                }
            }
            int c = nums[i];
            while(i < n-2 && nums[i] == c){i++;}
        }
        return res;
    }
};
