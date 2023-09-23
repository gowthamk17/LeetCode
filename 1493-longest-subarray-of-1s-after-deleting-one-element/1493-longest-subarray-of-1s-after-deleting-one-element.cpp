class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int maxSubLen = 0, l = 0, zero = 0;
        for(int r = 0; r < nums.size(); r++) {
            if(nums[r] == 0) {
                zero++;
            }
            while(zero > 1) {
                if(nums[l] == 0) {
                    zero--;
                }
                l++;
            }
            maxSubLen = max(maxSubLen, (r-l)+1);   
        }
        return --maxSubLen;
    }
};