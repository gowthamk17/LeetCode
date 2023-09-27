class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result;
        for(int i = 0; i < n+1; i++) {
            int num = i;
            int count = 0;
            while(num) {
                count += num % 2;
                num /= 2;
            }
            result.push_back(count);
        }
        return result;
    }
};