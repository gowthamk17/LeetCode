class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // int profit = 0, l = 0, r = 1;
        // while(r != prices.size()) {
        //     if(prices[l] < prices[r]) {
        //         int diff = prices[r] - prices[l];
        //         profit = max(profit, diff);
        //     } else {
        //         l = r;
        //     }
        //     r++;
        // }
        // return profit;
        
        int buyPrice = INT_MAX, maxProfit = 0;
        for(int i = 0; i < prices.size(); i++) {
            buyPrice = min(buyPrice, prices[i]);
            maxProfit = max(maxProfit, prices[i] - buyPrice);
        }
        return maxProfit;
    }
};