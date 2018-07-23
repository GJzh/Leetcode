class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int size = nums.size(), left, right, center;
        left = 0;
        right = size-1;
        while (left<=right)
        {
            if (left==right)
            {
                if (nums[left]==target){return left;}
                else{return (nums[left]<target)? left+1:left;}
            }
            else
            {
                center = (left+right)/2;
                if(nums[center]<target)
                {
                    left=center+1;
                }
                else if(nums[center]>target)
                {
                    right = center-1;
                }
                else
                {
                    return center;
                }
            }
        }
        return center;
    }
};
