class Solution {
public:
    int trap(vector<int>& height) 
    {
        int n = height.size();
        if (n <= 2) return 0;
        vector<int> left = vector<int>(n, 0);
        vector<int> right = vector<int>(n, 0);
        left[0] = height[0];
        right[n-1] = height[n-1];
        for (int i = 1; i < n; i++)
        {
            left[i] = max(left[i-1], height[i]);
        }
        for (int j = n - 2; j >= 0; j--)
        {
            right[j] = max(right[j+1], height[j]);
        }
        int res = 0;
        for (int k = 1; k < n - 1; k++)
        {
            res += max(min(left[k-1], right[k+1]) - height[k], 0);
        }
        return res;
    }
};
