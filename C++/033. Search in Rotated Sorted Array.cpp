class Solution {
private:
    int find(vector<int> &A, int target, int left, int right)
    {
        if (left > right) return -1;
        if (left == right) return (A[left] == target)? left:-1;
        int idx = -1;
        if (A[left] <= target && target <= A[right])
        {
            while(left <= right)
            {
                int mid = left + ((right - left) >> 1);
                if (A[mid] == target) return mid;
                else if (A[mid] < target)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }
        }
        else
        {
            int mid  = left + ((right - left) >> 1);
            if (A[mid] == target) return mid;
            else
            {
                idx = find(A, target, left, mid-1);
                return (idx == -1)? find(A, target, mid+1, right) : idx;
            }
        }
        return idx;
    }
public:
    int search(vector<int> &A, int target) 
    {
        // write your code here
        int n = A.size();
        return find(A, target, 0, n-1);
    }
};
