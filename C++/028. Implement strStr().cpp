class Solution {
public:
    bool compare(string& haystack, string& needle, int index)
    {
        for (int i = 0; i < needle.length(); i++)
        {
            if (haystack[index+i] != needle[i])
            {
                return false;
            }
        }
        return true;
    }
    int strStr(string haystack, string needle) 
    {
        int n = haystack.length();
        int m = needle.length();
        if(m > n) return -1;
        if (m == 0 && n == 0) return 0;
        for (int i = 0; i < n - m + 1; i++)
        {
            if (compare(haystack, needle, i))
            {
                return i;
            }
        }
        return -1;
    }
};
