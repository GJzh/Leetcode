class Solution {
private:
    double searchSortedArrays(vector<int>& nums1, vector<int>& nums2, int A_st, int B_st, int k)
    {
        if(A_st>=nums1.size()){return nums2[B_st+k-1];}
        if(B_st>=nums2.size()){return nums1[A_st+k-1];}
        if(k==1){return min(nums1[A_st],nums2[B_st]);}
        int A_key = (A_st+k/2-1<nums1.size())? nums1[A_st+k/2-1]:INT_MAX;
        int B_key = (B_st+k/2-1<nums2.size())? nums2[B_st+k/2-1]:INT_MAX;
        if(A_key<=B_key)
        {
            return searchSortedArrays(nums1, nums2, A_st+k/2, B_st, k-k/2);
        }
        else
        {
            return searchSortedArrays(nums1, nums2, A_st, B_st+k/2, k-k/2);
        }
    }
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1=nums1.size();
        int n2=nums2.size();
        int sum = n1+n2;
        if(sum&1==1)
        return searchSortedArrays(nums1, nums2, 0, 0, sum/2+1);
        else
        {
            return (searchSortedArrays(nums1, nums2, 0, 0, sum/2)+searchSortedArrays(nums1, nums2, 0, 0, sum/2+1))/2.0;
        }
    }
};
