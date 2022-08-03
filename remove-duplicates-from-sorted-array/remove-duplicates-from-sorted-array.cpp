class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int unique = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[unique] != nums[i]){
                nums[++unique] = nums[i];
            }
        }
     return ++unique;
    }
};