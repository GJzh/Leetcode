class Solution {
private:
void CombinationPar(vector<string>& result, string& sample, int deep, int n, int leftNum, int rightNum)
{
    if (deep==2*n)
    {
        result.push_back(sample);
        return;
    }
    if(leftNum<n)
    {
        sample.push_back('(');
        CombinationPar(result, sample, deep+1, n, leftNum+1, rightNum);
        sample.resize(sample.length()-1);
    }
    if(leftNum>rightNum)
    {
        sample.push_back(')');
        CombinationPar(result, sample, deep+1, n, leftNum, rightNum+1);
        sample.resize(sample.length()-1);
    }
}
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string sample;
        if(n!=0)
        {
            CombinationPar(res, sample, 0, n, 0, 0);
        }
        return res;
    }
};
