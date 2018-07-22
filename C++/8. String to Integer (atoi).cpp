class Solution {
public:
    int myAtoi(string str) {
        int size = str.length();
        int result=0;
        long long temp=0;
        int f=1;
        if(size==0)
        {
            return 0;
        }
        int i=0;
        while(i<size)
        {
            if(str[i]==' ')
            {
                ++i;
            }
            else if ((str[i]=='+' || str[i]=='-') && (str[i+1]<='9' && str[i+1]>='0'))
            {
                f=(str[i]=='-')? -1:1;
                for(int j=i+1;j<=i+12;j++)
                {
                    if(str[j]<='9' && str[j]>='0')
                    {
                        temp=10*temp+str[j]-'0';
                    }
                    else
                    {
                        break;
                    }
                }
                break;
            }
            else if (str[i]<='9' && str[i]>='0')
            {
                for(int j=i;j<=i+12;j++)
                {
                    if(str[j]<='9' && str[j]>='0')
                    {
                        temp=10*temp+str[j]-'0';
                    }
                    else
                    {
                        break;
                    }
                }
                break;
            }
            else
            {
                return 0;;
            }
        }
        temp*=f;
        if(temp>INT_MAX)
        {
            result=INT_MAX;
        }
        else if(temp<INT_MIN)
        {
            result=INT_MIN;
        }
        else
        {
            result = (int)temp;
        }
        return result;
    }
};
