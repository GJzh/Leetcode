class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int size = nums.size();
        if(size<=1){return;}
        int index1=size-1;
        while(index1>0)
        {
            if(nums[index1]>nums[index1-1]){break;}
            index1--;
        }
        if(index1==0)
        {
            sort(nums.begin(),nums.end());
            return;
        }
        int index2=size-1;
        while(index2>=index1)
        {
            if (nums[index2]>nums[index1-1]){break;}
            index2--;
        }
        swap(nums[index1-1],nums[index2]);
        sort(nums.begin()+index1,nums.end());
        return;
    }
};
