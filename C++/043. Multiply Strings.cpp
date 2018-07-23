class Solution {
public:
    string multiply(string num1, string num2) 
    {
        int m = num1.length();
        int n = num2.length();
        if (m * n == 0) return "";
        if (m == 1 && num1[0] == '0') return "0";
        if (n == 1 && num2[0] == '0') return "0";
        int carry = 0;
        string res(m + n, '0');
        for (int k = m + n - 1; k >= 0; k--)
        {
            int val = carry;
            for (int i = max(0, k - n); i <= min(m - 1, k - 1); i++)
            {
                val += (num1[i] - '0') * (num2[k - 1 -i] - '0');
            }
            res[k] = (val % 10) + '0';
            carry = val / 10;
        }
        if (res[0] == '0')
        {
            res = res.substr(1);
        }
        return res;
    }
};
