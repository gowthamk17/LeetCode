class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int result = 0;
        
        for(int i : nums){
            if(i == 0) count = 0;
            else{
                count++;
                if(count > result) result = count;
            }
        }
        
        
        
        return result;
    }
};