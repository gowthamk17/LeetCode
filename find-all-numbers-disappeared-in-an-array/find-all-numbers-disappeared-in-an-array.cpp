class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> hash;
        vector<int> result;
        for(int i=1; i<=nums.size()+1; i++){
            hash.push_back(0);
        }
        for(int i=0; i<nums.size();i++){
            hash[nums[i]] = 1;
        }
        for(int i=1; i<=nums.size(); i++){
            if(hash[i] == 0) 
                result.push_back(i);
        }
        
        return result;
    }
};