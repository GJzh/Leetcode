class Solution {
private:
    bool checkSubstring(string &s,unordered_map<string,int> &hash, int k, int m, int L, int N)
    {
        bool res;
        string word = s.substr(k,m);
        //cout << "word=" << word << "\n";
        if(!hash[word])
        {
            return false;
        }
        if(L+1==N)
        {return true;}
        else
        {
            hash[word]--;
            res = checkSubstring(s,hash,k+m,m,L+1,N);
            hash[word]++;
            return res;
        }
    }
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res={};
        int n = s.length(), size = words.size();
        if(!n||!size){return res;}
        int m = words[0].length();
        unordered_map<string,int> hash;
        for (int j=0;j<size;j++)
        {
            hash[words[j]]+=1;
        }
        for (int i=0;i<=n-m*size;i++)
        {
            if(checkSubstring(s,hash,i,m,0,size))
            {
                res.push_back(i);
            }
        }
        return res;
    }
};
