class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min(prices[0], prices[1])
        min2 = max(prices[0], prices[1])
        
        for i in range(2, len(prices)):
            if prices[i] < min1:
                min2 = min1
                min1 = prices[i]
            elif prices[i] < min2:
                min2 = prices[i]
        
        leftover = money-min1-min2 if (money-min1-min2) >= 0 else money
        return leftover