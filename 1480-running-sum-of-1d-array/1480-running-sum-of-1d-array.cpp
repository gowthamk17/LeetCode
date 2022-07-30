class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        
//    this code directly changes the values of the source array
        
//     int runv = 0;
//     for (int &i : nums){
//         i += runv;
//         runv = i;
//     }  
//     return nums;    
//     }
        
    vector<int> result = {nums[0]};
    for(int i = 1; i < nums.size(); i++){
        result.push_back(nums[i] + result.back());
    }
    return result;   
    }
};