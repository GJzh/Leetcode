class Solution {
public:
    int jump(vector<int>& nums) {
        int n=nums.size();
        if(n<=1){return 0;}
        int lindex=0, hindex=0, minstep=0;
        while(lindex<=hindex)
        {
            int lasthindex=hindex;
            minstep++;
            for(int i=lindex;i<=lasthindex;i++)
            {
                int possibledist=i+nums[i];
                if(possibledist>=n-1){return minstep;}
                hindex=max(hindex,possibledist);
            }
            lindex=lasthindex+1;
        }
        return minstep;
    }
};
