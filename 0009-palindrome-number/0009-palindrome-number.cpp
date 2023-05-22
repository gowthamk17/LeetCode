class Solution {
public:
    bool isPalindrome(int x) {
        string num = to_string(x);
        int i = 0, n = num.size() - 1;
        while(i < n) {
            if(num[i] != num[n]) return false;
            i++;
            n--;
        }
        return true;
    }
};