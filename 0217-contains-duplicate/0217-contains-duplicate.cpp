class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> u_nums;
        for(int i = 0; i < nums.size(); i++){
            if(u_nums.find(nums[i]) == u_nums.end()){
                u_nums.insert(nums[i]);
            }
            else{
                return true;
            }
        }
        return false;
    }
};