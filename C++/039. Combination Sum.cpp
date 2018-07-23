class Solution {
private: 
    void SearchSum(vector<vector<int>> &res, vector<int>& candidates, vector<int>& sol, int target, int index)
    {
        for(int j=index;candidates[j]<=target && j < candidates.size();j++)
        {
            
            if (candidates[j]<=target)
            {
                sol.push_back(candidates[j]);
                if(candidates[j]==target)
                {
                    res.push_back(sol);
                    sol.pop_back();
                    return;
                }
                else
                {
                    SearchSum(res, candidates, sol, target-candidates[j], j);
                    sol.pop_back();
                }
            }
            else{break;}
        }
        return;
    }

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> sol;
        vector<vector<int>> res;
        int size = candidates.size();
        if (size<=0){return res;}
        sort(candidates.begin(),candidates.end());
        SearchSum(res, candidates, sol, target, 0);
        return res;
    }
};
