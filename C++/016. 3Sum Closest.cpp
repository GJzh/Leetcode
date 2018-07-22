class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int res=nums[0]+nums[1]+nums[2]-target;
        int diff=abs(nums[0]+nums[1]+nums[2]-target);
        int size = nums.size();
        int left,right;
        sort(nums.begin(),nums.end());
        for (int i=0;i<size-2;i++)
        {
            left = i+1;
            right = size-1;
            while(left<right)
            {
                diff = nums[i]+nums[left]+nums[right]-target;
                if (abs(diff)<abs(res))
                {
                    res = diff;
                }
                if(diff<0){left++;}
                else if(diff>0){right--;}
                else
                {
                    return target;
                }
            }
            while(nums[i+1]==nums[i]){i++;}
        }
        res += target;
        return res;
    }
};
