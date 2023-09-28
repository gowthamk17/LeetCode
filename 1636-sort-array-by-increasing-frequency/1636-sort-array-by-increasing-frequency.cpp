class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        std::vector<int> array;
        std::map<int, int, greater<int>> map;
        for(int n : nums) {
            map[n]++;
        }
        int j = 1;
        while(j <= nums.size()) {
            for(auto i: map) {
                if(i.second == j) {
                    for(int k = 0; k < j; k++) {
                        array.push_back(i.first);
                    }
                }
            }
            if(nums.size() == array.size()) {
                break;
            }
            j++;
        }
        return array;
    }
};