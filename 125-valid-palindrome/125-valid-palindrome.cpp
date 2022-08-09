class Solution {
public:
    bool isPalindrome(string s) {
        string rstr;
        for(char c: s){
            if(isalnum(c))
                rstr.push_back(tolower(c));   
        }
        if(rstr.empty()) return true;
        string tmp_rstr = rstr;
        reverse(rstr.begin(),rstr.end());
        return tmp_rstr == rstr;
    }
};