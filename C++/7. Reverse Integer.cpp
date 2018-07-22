class Solution {
public:
    int reverse(int x) {
        long long result = 0;
        int num;
        int f;
        if(x==0)
        {
            return 0;
        }
        else if(x>0)
        {
            f=1;
        }
        else
        {
            f=-1;
        }
        x*=f;
        for(int i=1;;i++)
        {
            num = x%10;
            result = 10*result+num;
            x = (x-num)/10;
            if(x==0)
            {
                break;
            }
        }
        result *= f;
        return (result<INT_MIN || result>INT_MAX)? 0:(int)result;
    }
};
