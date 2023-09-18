class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        std::unordered_map<int, int> numsMap;
        int count = 0;
        for(int n : nums) {
            int diff = k - n;
            if(numsMap[diff] && numsMap[diff] > 0) {
                count++;
                numsMap[diff]--;
            } else {
                numsMap[n] = numsMap[n] ? numsMap[n]+1 : 1;
            }
        }
        return count;
    }
};