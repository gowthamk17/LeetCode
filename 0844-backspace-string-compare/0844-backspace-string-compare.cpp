class Solution {
public:
    bool backspaceCompare(string s, string t) {
        s = removeBackSpace(s);
        t = removeBackSpace(t);
        return s==t;
    }
    std::string removeBackSpace(string s) {
        string finalString  = "";
        for(char c : s) {
            if(c == '#') {
                if(!finalString.empty()) {
                    finalString.pop_back();
                }
            } else {
                finalString.push_back(c);
            }
        }
        return finalString;
    }
};