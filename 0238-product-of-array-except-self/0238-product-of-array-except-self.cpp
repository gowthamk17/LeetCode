class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n);
    int pre = 1, post = 1;
    result[0] = 1;
    for(int i = 0; i < n -1; i++) {
        pre *= nums[i];
        result[i+1] = pre;
    }
    for(int i = n -1; i > 0; i--) {
        post *= nums[i];
        result[i-1] *= post;
    }
    return result;
    }
};