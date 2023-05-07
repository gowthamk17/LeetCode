class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // solution 1
        // vector<int> result;
        // for(int k = 0; k < nums.size() - 1; k++) {
        //     for(int l = k + 1; l < nums.size(); l++) {
        //         if(nums[k] + nums[l] == target) {
        //             result.push_back(k);
        //             result.push_back(l);
        //             break;
        //         }
        //     }
        //     if(!result.empty()) {
        //         break;
        //     }
        // }
        // return result;
        
        // solution 2
        
        unordered_map<int, int> map;
        vector<int> result = {-1, -1};
        for(int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if(map.find(diff) != map.end()) {
                result[0] = map[diff];
                result[1] = i;
                break;
            }
            map[nums[i]] = i;
        }
        return result;   
    }
};