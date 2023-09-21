class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, r = 0, count = 0, ans = 0;
        for(;r<nums.size();r++) {
            if(nums[r] == 0) count++;
            while(count > k) {
                if(nums[l] == 0) count--;
                l++;
            }
            ans = max(ans, (r-l)+1);
        }
        return ans;
    }
};