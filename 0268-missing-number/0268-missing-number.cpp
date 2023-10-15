class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> set;
        for(int i : nums) {
            set.insert(i);
        }
        for(int i = 0; i <= n; i++) {
            if(set.find(i) == set.end()) {
                return i;
            }
        }
        return -1;
    }
};