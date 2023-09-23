class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int maxSubLen = 0, l = 0, zero = 0;
        for(int r = 0; r < nums.size(); r++) {
            // if(nums[r] == 0) {
            //     zero++;
            // }
            zero += (nums[r] == 0);
            while(zero > 1) {
                // if(nums[l] == 0) {
                //     zero--;
                // }
                zero -= (nums[l] == 0);
                l++;
            }
            maxSubLen = max(maxSubLen, (r-l));   
        }
        return maxSubLen;
    }
};