class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size=nums.size();
        int j=size-1;
        int i=0;
        if (size==0)
        {
            return 0;
        }
        while (j-i>=0)
        {
            if(nums[i]==val)
            {
                nums[i]=nums[j];
                --j;
            }
            else
            {
                ++i;
            }
        }
        return i;
    }
};
