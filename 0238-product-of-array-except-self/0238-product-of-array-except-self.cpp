class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n,1);
    int pre = 1, post = 1;
    for(int i = 0; i < n; i++) {
        result[i] *= pre;
        pre *= nums[i];
        result[n-1-i] *= post;
        post *= nums[n-1-i];   
    }
    return result;
    }
};