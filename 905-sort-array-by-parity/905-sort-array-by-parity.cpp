class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int i = 0, j = 0, n = nums.size();
        while(i < n){
            if(nums[i] % 2 ==0){
                swap(nums[j],nums[i]);
                j++;
                i++;
            }else i++;
        }
        return nums;
    }
};