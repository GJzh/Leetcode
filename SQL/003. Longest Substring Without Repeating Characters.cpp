class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> hash;
        int res=0,L=0;
        int start=-1;
        for(int i=0;i<s.length();i++)
        {
            if(hash.find(s[i])!=hash.end() && hash[s[i]]>=start)
            {
                res=max(res,L);
                start=hash[s[i]]+1;
                L = i-hash[s[i]];
                hash[s[i]]=i;
            }
            else
            {
                hash[s[i]]=i;
                L++;
            }
        }
        return max(res,L);
    }
};
