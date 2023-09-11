class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        std::set<int> num1_set;
        for(int n : nums1) {
            num1_set.insert(n);
        }
        std::set<int> num2_set;
        for(int n : nums2) {
            num2_set.insert(n);
        }
        vector<int> num1;
        for(int n : num1_set) {
            auto it = std::find(num2_set.begin(), num2_set.end(), n);
            if(it == num2_set.end()) {
                num1.push_back(n);
            }
        }
        vector<int> num2;
        for(int n : num2_set) {
            auto it = std::find(num1_set.begin(), num1_set.end(), n);
            if(it == num1_set.end()) {
                num2.push_back(n);
            }
        }
        vector<vector<int>> result;
        result.push_back(num1);
        result.push_back(num2);
        return result;
    }
};