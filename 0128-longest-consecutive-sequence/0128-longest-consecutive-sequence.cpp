class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> mySet(nums.begin(), nums.end());
        int longest;
        for(auto &n : mySet) {
            int length = 0;
            if(mySet.find(n-1) == mySet.end()) {
                while(mySet.find(n+length) != mySet.end()) {
                    length++;
                }
                longest = std::max(longest, length);
            }
        }
        return longest;
    }
};