class Solution {
private:
    int searchLeftBound(vector<int>& nums, int left, int right, int target)
    {
        int center;
        while(left<=right)
        {
            if(left==right){return left;}
            center =(left+right)/2;
            if(nums[center]<target)
            {
                left=center+1;
            }
            else
            {
                right=center;
            }
        }
        return left;
    }
    int searchRightBound(vector<int>& nums, int left, int right, int target)
    {
        int center;
        while(left<=right)
        {
            if(left==right){return left;}
            center =(left+right)/2;
            if(nums[center]>target)
            {
                right=center-1;
            }
            else
            {
                if (left!=center){left=center;}
                else
                {
                    return (nums[right]==target)? right:left;
                }
            }
        }
        return left;
    }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2,-1);
        int size = nums.size();
        int left=0, right= size-1, center, c1, c2;
        while(left<=right)
        {
            if(left==right)
            {
                if(nums[left]==target)
                {
                    res[0]=left;
                    res[1]=right;
                    return res;
                }
                return res;
            }
            center = (left+right)/2;
            if(nums[center]<target)
            {
                left = center+1;
            }
            else if(nums[center]>target)
            {
                right = center;
            }
            else{break;}
        }
        res[0] = searchLeftBound(nums, left, center, target);
        res[1] = searchRightBound(nums, center, right, target);
        return res;
    }
};
