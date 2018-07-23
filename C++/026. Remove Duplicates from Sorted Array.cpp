class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int j=0;
        int size = nums.size();
        if(size<=1)
        {
            return size;
        }
        for(int i=0;i<size-1;i++)
        {
            if(nums[j]<nums[i+1])
            {
                nums[j+1]=nums[i+1];
                ++j;
            }
        }
        return j+1;
    }
};
