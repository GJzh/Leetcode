class Solution {
public:
    int reversePairs(vector<int>& nums) 
    {
        int n = nums.size();
        vector<int> v = nums;
        sort(v.begin(), v.end());
        unordered_map<int,int> pos;
        for (int i = 0; i < n; i++) {pos[v[i]]=i+1;}
        vector<int> bit(n+1);
        int res = 0;
        for (int i = n-1; i >= 0; i--)
        {
            int k = lower_bound(v.begin(), v.end(), nums[i]/2.0) - v.begin();
            res += getSum(bit, k);
            update(bit, pos[nums[i]]);
        }
        return res;
    }
    
    void update(vector<int>& bit, int i)
    {
        int n = bit.size();
        while(i < n)
        {
            bit[i]++;
            i += (i&-i); 
        }
    }
    
    int getSum(vector<int>& bit, int i)
    {
        int res = 0;
        while(i > 0)
        {
            res += bit[i];
            i -= (i&-i); 
        }
        return res;
    }
};
