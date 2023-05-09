class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>>  map;
        for(int i = 0; i < strs.size(); i++) {
            string key = getKey(strs[i]);
            map[key].push_back(strs[i]);

        }
        vector<vector<string>> output;
        for(auto it = map.begin(); it != map.end(); it++) {
            output.push_back(it->second);
        }
        return output;
    }
private:
    string getKey(string str){
        int freq[26] = {0};
        for(int i = 0; i < str.size(); i++) {
            freq[str[i] - 'a']++;
        }
        string key = "";
        for(int i = 0; i < 26; i++) {
            key.append(to_string(freq[i] + 'a'));
        }
        return key;
    }
};