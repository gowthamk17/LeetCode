class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> mySet(nums.begin(), nums.end());
        int longest;
        for(auto &n : mySet) {
            int length = 0;
            if(!mySet.count(n - 1)) {
                ++length;
                while(mySet.count(n+length)) {
                    ++length;
                }
                longest = std::max(longest, length);
            }
        }
        return longest;
    }
};