class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double total = 0;
        for(int i = 0; i < k; i++) {
            total += nums[i];
        }
        double res = total;
        for(int i = k; i < nums.size(); i++) {
            total += nums[i] - nums[i-k];
            res = max(res, total);
        }
        return res/k;
    }
};