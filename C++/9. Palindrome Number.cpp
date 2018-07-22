class Solution {
public:
    bool isPalindrome(int x) {
        int xtemp=x;
        int power=1;
        if(x>INT_MAX || x<0)
        {
            return false;
        }
        if(x<10)
        {
            return true;
        }
        while(xtemp/10>0)
        {
            power *=10; 
            xtemp/=10;
        }
        if(power==1)
        {
            return true;
        }
        while(power>1)
        {
            if( x%10 != x/power )
            {
                return false;
            }
            else
            {
                x=x%power/10;
                power/=100;
            }
        }
        return true;
    }
};
