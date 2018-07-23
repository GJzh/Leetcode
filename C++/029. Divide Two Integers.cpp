class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend>INT_MAX || dividend<INT_MIN || divisor>INT_MAX || divisor<INT_MIN){return INT_MAX;}
        long long res=0;
        unsigned long val1,val2,temp1,temp2;
        val1 = (dividend>=0)? dividend:-(long long)dividend; 
        val2 = (divisor>=0)? divisor:-(long long)divisor; 
        temp1 = val1;
        temp2 = val2;
        long long c = 1;
        if(val1 < val2){return 0;}
        while(val1 >= temp2)        
        {
            temp2 = temp2 << 1;
            c= c << 1;
        }
        while(temp1>=val2)
        {
            while(temp1>=temp2)
            {
                temp1 -= temp2;
                res += c; 
            }
            temp2 = temp2 >> 1;
            c = c>>1;
        }
        
        if((dividend<0 && divisor>0) || (dividend>0 && divisor<0))
        {
            res = 0-res;
        }
        if(res>INT_MAX ||res<INT_MIN)
        {
            return INT_MAX;
        }
        else
        {
            return (int)res;
        }
    }
};
