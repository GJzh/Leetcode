class Solution {
public:
    bool isValid(string s) 
    {
        int n = s.length();
        if (n == 0) return true;
        stack<char> myStack;
        for (int i = 0; i < n; i++)
        {
            char cur = s[i];
            if (cur == '(' || cur == '[' || cur == '{')
            {
                myStack.push(cur);
            }
            else if (!myStack.empty() )
            {
                char old  = myStack.top();
                if ((old == '(' && cur == ')') || (old == '[' && cur == ']') || (old == '{' && cur == '}') )
                {
                    myStack.pop();
                }
                else
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        return myStack.empty();
    }
};
