class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int N = nums.size();
        int lastNonZero = 0;
        for(int i = 0; i < N; i++){
            if(nums[i] != 0){
                nums[lastNonZero++] = nums[i];
            }
        }
        for(;lastNonZero<N;lastNonZero++){
            nums[lastNonZero] = 0;
         }
        
    }
};