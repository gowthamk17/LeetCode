class Solution {
public:
    int maxVowels(string s, int k) {
        std::unordered_set vowel{'a','e','i','o','u'};
        int result = 0;
        int count = 0;
        for(int i = 0; i < k; i++) {
            count += vowel.count(s[i]);
        }
        result = count;
        for(int i = k; i < s.size(); i++) {
            count += vowel.count(s[i]) - vowel.count(s[i-k]);
            result = max(result, count);
        }
        return result;
    }
};