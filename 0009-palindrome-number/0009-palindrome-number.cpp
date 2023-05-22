class Solution {
public:
    bool isPalindrome(int x) {
        string num = to_string(x);
        for(int i = 0; i < num.size(); i++) {
            int n = num.size() - 1 - i;
            if(i >= n) break;
            if(num[i] != num[n]) return false;
        }
        return true;
    }
};