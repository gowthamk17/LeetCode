class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int N = heights.size();
        vector<int> ans = heights;
        int exp = 0;
        sort(ans.begin(),ans.end());
        
        
        for(int i = 0; i<N; i++){
            if(heights[i] != ans[i]) exp++;
        }   
        return exp;
    }
};