class Solution {
public:
    bool isUgly(int n) {
        if(n == 0) return false;
        bool canDivide = true;
        while(canDivide) {
            if(n%2 == 0) {
                n /= 2;
            } else if(n%3 == 0) {
                n /= 3;
            } else if(n%5 == 0) {
                n /= 5;
            } else {
                canDivide = false;
            }
        }
        return n == 1;
    }
};