class Solution {
public:
    int romanToInt(string s) {
        int size=s.size();
        int result=0;
        string t = "MDCLXVI";
        int roman [7] = {1000,500,100,50,10,5,1};
        int temp = 0;
        int index[size];
        index[0] = t.find(s[0]);
        for(int i=0;i<size-1;i++)
        {
            index[i+1] = t.find(s[i+1]);
            temp += roman[index[i]];
            if(index[i+1]>index[i])
            {
                result += temp;
                temp = 0;
            }
            else if (index[i+1]<index[i])
            {
                result -= temp;
                temp = 0;
            }
        }
        result += (roman[index[size-1]] + temp);
        return result;
    }
};
