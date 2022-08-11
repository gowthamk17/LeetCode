class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int m = 0, mIndex;
        for(int i = 0; i<nums.size(); i++){
            if(nums[i] > m){
                m = nums[i];
                mIndex = i;
            }
        }
        
        for(int j = 0; j<nums.size(); j++){
            if(nums[j] != m and m < 2 * nums[j]) return -1;
        }
        
        
        return mIndex;
    }
};