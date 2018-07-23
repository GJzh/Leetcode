class Solution {
public:
    int longestValidParentheses(string s) {
        int res=0,temp;
        int n = s.length();
        vector<int> state(n,0);
        stack<pair<char,int>> H;
        for(int i=0;i<n;i++)
        {
            while(s[i]==')'){i++;}
            while(i<n)
            {
                if(s[i]=='('){H.push(make_pair(s[i],i));i++;}
                else
                {
                    if (!H.empty())
                    {
                        state[H.top().second]=1;
                        state[i]=1;
                        H.pop();
                        i++;
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            temp=0;
            while(i<n && !state[i]){i++;}
            while(i<n && state[i])
            {
                temp++;
                i++;
            }
            res = max(temp,res);
        }
        return res;
    }
};
