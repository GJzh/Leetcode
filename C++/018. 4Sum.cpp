class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        int size = nums.size();
        int left,right,val1,val2;
        sort(nums.begin(),nums.end());
        for(int i=0;i<size-3;i++)
        {
            for(int j=i+1;j<size-2;j++)
            {
                left=j+1;
                right=size-1;
                val1 = nums[i]+nums[j];
                while(left<right)
                {
                    val2 = nums[left]+nums[right];
                    if(val1+val2<target)
                    {
                        left++;
                    }
                    else if(val1+val2>target)
                    {
                        right--;
                    }
                    else
                    {
                        vector<int> sol(4,0);
                        sol[0] = nums[i];
                        sol[1] = nums[j];
                        sol[2] = nums[left];
                        sol[3] = nums[right];
                        res.push_back(sol);
                        while(left<right && nums[left]==sol[2]){left++;}
                        while(left<right && nums[right]==sol[3]){right--;}
                    }
                }
                while(j<size-2 && nums[j+1]==nums[j]){j++;}
                if(target-nums[i]-nums[j]<2*nums[j+1]){break;}
            }
            while(i<size-3 && nums[i+1]==nums[i]){i++;}
        }
        return res;
    }
};
