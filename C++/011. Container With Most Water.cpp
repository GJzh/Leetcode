class Solution {
public:
    int maxArea(vector<int>& height) {
        int res=0;
        int size = height.size();
        int left = 0;
        int right = size-1;
        int area=0;
        while(right-left>0)
        {
            area = min(height[left],height[right])*(right-left);
            if(area>res)
            {
                res=area;
            }
            if(height[left]<height[right]){left++;}
            else if(height[left]>height[right]){right--;}
            else
            {
                left++;
                right--;
            }
        }
        return res;
    }
};
