class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0, j = 0, n = nums.size();
        while(i < n){
            if(nums[i] != val){
                swap(nums[j],nums[i]);
                i++;
                j++;
            }else i++;
        }
        
        return j;
    }
};