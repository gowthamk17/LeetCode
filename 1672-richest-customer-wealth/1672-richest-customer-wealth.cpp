class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int wealthiest = 0;
        for(auto i : accounts){
            int total = 0;
            for(auto j : i){
                total += j;
            }
            if(total > wealthiest){
                wealthiest = total;
            }
        }
        return wealthiest;
    }
};