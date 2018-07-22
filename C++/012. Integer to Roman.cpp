class Solution {
public:
    string intToRoman(int num) {
        string result="";
        string t = "MDCLXVI";
        int base = 0;
        int rest;
        int count;
        int roman [7] = {1000,500,100,50,10,5,1};
        for(int i=0;i<7;i++)
        {
            if(num>=roman[i])
            {
                base = i;
                break;
            }
        }
        if(base%2==0)
        {
            if(num<4*roman[base])
            {
                for(int j=0;j<num/roman[base];j++)
                {
                    result += t[base];
                }
                rest = num-num/roman[base]*roman[base];
                if(rest>0)
                {
                    result += intToRoman(rest);
                }
            }
            else
            {
                result += t[base];
                result += t[base-1];
                rest = num-4*roman[base];
                if(rest>0)
                {
                    result += intToRoman(rest);
                }
            }
        }
        else
        {
            if(num<roman[base]+4*roman[base+1])    
            {
                result += t[base];
                count = (num-roman[base])/roman[base+1];
                for(int j=0;j<count;j++)
                {
                    result += t[base+1];
                }
                rest = num-roman[base]-count*roman[base+1];
                if(rest>0)
                {
                    result += intToRoman(rest);
                }
            }
            else
            {
                result += t[base+1];
                result += t[base-1];
                rest = num-9*roman[base+1];
                if(rest>0)
                {
                    result += intToRoman(rest);
                }
            }
        }
        
        return result;
    }
};
