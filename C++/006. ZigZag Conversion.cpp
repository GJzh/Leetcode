class Solution {
public:
    string convert(string s, int numRows) {
        string result;
        int size = s.size();
        int skipelements1;
        if(numRows==1)
        {
            skipelements1 = 1;
        }
        else
        {
            skipelements1 = numRows + numRows-2;
        }
        int skipelements2;
        int index1;
        int index2;
        for(int i=0;i<numRows;i++)
        {
            for(int j=0;;j++)
            {
                index1=i+skipelements1*j;
                if(index1<size)
                {
                    result += s[index1];
                }
                else
                {
                    break;
                }
                if(i!=0 && i!=numRows-1)
                {
                    skipelements2 = 2*(numRows-1-i);
                    index2=index1+skipelements2;
                    if(index2<size)
                    {
                        result += s[index2];
                    }
                    else
                    {
                        break;
                    }
                }
                
            }
            
        }
        return result;
    }
};
