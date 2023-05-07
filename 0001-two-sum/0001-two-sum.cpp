class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(int k = 0; k < nums.size() - 1; k++) {
            for(int l = k + 1; l < nums.size(); l++) {
                if(nums[k] + nums[l] == target) {
                    result.push_back(k);
                    result.push_back(l);
                    break;
                }
            }
            if(!result.empty()) {
                break;
            }
        }
        return result;
    }
};