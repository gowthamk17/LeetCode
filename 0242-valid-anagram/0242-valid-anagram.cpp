class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) {
            return false;
        }
        
        // solution 1
        // sort(s.begin(), s.end());
        // sort(t.begin(), t.end());
        // for(int i = 0; i < s.length(); i++)  {
        //     if(s[i] != t[i]) {
        //         return false;
        //     }
        // }
        // return true;
        
        // solution 2
        int freq[26] = {0};
        for(int i = 0; i < s.length(); i++) {
            freq[s[i] - 'a']++;
            freq[t[i] - 'a']--;
        }
        for(int i = 0; i < 26; i++) {
            if(freq[i] != 0) {
                return false;
            }
        }
        return true;
    }
};