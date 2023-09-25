class Solution {
public:
    bool isHappy(int n) {
        // if(n < 10) {
        //     if(n==1 || n==7) {
        //         return true;
        //     } else {
        //         return false;
        //     }
        // }
        // int squareSum = getSquareSum(n);
        // return isHappy(squareSum);
        
        set<int> visited;
        while(true) {
            n = getSquareSum(n);
            if(n==1) return true;
            if(visited.find(n) != visited.end()) return false;
            visited.insert(n);
        }
        return false;
    }
    int getSquareSum(int n) {
        int sum = 0;
        while(n) {
            int x = n % 10;
            sum += (x * x);
            n/=10;
        }
        return sum;
    }
};