class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        std::unordered_map<int, int> numsMap;
        int count = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(numsMap[k-nums[i]] && numsMap[k-nums[i]] > 0) {
                count++;
                numsMap[k-nums[i]]--;
            } else {
                numsMap[nums[i]] = numsMap[nums[i]] ? numsMap[nums[i]]+1 : 1;
            }
        }
        return count;
    }
};