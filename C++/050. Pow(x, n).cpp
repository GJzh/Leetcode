class Solution {
public:
    double myPow(double x, int n) 
    {
        if (n == 0) return 1;
        else if (n == 1) return x;
        else if (n == -1 && x != 0) return 1/x;
        double temp1 = myPow(x, n>>1);
        double temp2 = myPow(x, n&1);
        return temp1 * temp1 * temp2;
    }
};
