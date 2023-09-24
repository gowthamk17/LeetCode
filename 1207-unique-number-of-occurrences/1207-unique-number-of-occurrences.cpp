class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map<int, int> countMap;
        for(int item : arr) {
            countMap[item]++;
        }
        std::unordered_set<int> values;
        for(const auto i: countMap) {
            if(values.count(i.second)){
                return false;
            } else {
                values.insert(i.second);
            }
        }
        return true;
    }
};