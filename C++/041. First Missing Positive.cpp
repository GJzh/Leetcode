class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        if(!n){return 1;}
        unordered_map<int,int> hash;
        for(int i=0;i<n;i++)
        {
            hash[nums[i]]=1;
        }
        int res=1;
        while(hash[res]){res++;}
        return res;
    }
};
