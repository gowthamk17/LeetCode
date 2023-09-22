class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int ans = 0;
        int n = arr.size();
        for(int left = 0; left < n; left++) {
            int curSum = 0;
            for(int right = left; right < n; right++) {
                curSum += arr[right];
                ans += (right-left+1) % 2 == 1 ? curSum : 0;
            }
        }
        return ans;
    }
};