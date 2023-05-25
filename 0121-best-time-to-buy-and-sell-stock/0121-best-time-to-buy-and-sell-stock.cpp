class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, l = 0, r = 1;
        while(r != prices.size()) {
            if(prices[l] < prices[r]) {
                profit = max(profit, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }
        return profit;
    }
};