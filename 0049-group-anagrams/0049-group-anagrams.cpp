class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> output;
        if(strs.size() == 1) {
            output.push_back(strs);
            return output;
        }
        unordered_map<string, vector<string>>  map;
        for(int i = 0; i < strs.size(); i++) {
            string str = strs[i];
            sort(str.begin(), str.end());
            if(map.find(str) != map.end()) {
                map[str].push_back(strs[i]);
            } else {
                vector<string> strList = {strs[i]};
                map[str] = strList;
            }  
        }
        for(const auto &[key, value] : map) {
            output.push_back(value);
        }
        return output;
    }
};