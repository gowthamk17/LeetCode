class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if(nums.size() < 3) {
            return false;
        }
        int i = INT_MAX, j = INT_MAX;
        for(int l = 0; l < nums.size(); l++) {
            if(nums[l] <= i) {
                i = nums[l];
            } else if(nums[l] <= j) {
                j = nums[l];
            } else {
                return true;
            }
        }
        return false;
    }
};