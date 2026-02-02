class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_diff = 0
        for price in prices:
            diff = price-min_price
            if price<min_price:
                min_price = price
            max_diff = max(max_diff, diff)

        return max_diff