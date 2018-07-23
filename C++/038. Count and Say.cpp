class Solution {
public:
    string transform(string s)
    {
        string res = "";
        int n = s.length();
        int count = 1;
        char c = s[0];
        for (int i = 1; i < n; i++)
        {
            if (s[i] == c)
            {
                count++;
            }
            else
            {
                res += to_string(count);
                res += c;
                c = s[i];
                count = 1;
            }
        }
        res += to_string(count);
        res += c;
        return res;
    }
    string countAndSay(int n) {
        if(n==0) return "";
        string res = "1";
        for (int i = 1; i< n; i++)
        {
            res = transform(res);
        }
        return res;
    }
};
