class Solution {
public:
    int arrangeCoins(int n) {
        int stairs = 0;
        int i = 1;
        while(n > 0) {
            if(n >= i){
                stairs++;
            }
            n -= i;
            i++;
        }
        return stairs;
    }
};