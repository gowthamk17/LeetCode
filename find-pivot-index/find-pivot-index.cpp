class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if(nums.size() == 1) return nums[0];
        int tSum = 0,index = 0,lSum,rSum;
        for(int i = 0; i < nums.size(); i++){
            tSum += nums[i]; 
        }
        while(index < nums.size()){
            if(index==0) lSum = 0;
            else lSum += nums[index-1];
            if(index==nums.size()-1) rSum = 0;
            else rSum = tSum - lSum - nums[index];
            if(lSum == rSum) return index;
            index++;
        }
        return -1;
    }
};
