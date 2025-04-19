class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = prices[0]
        for i in range(1, len(prices)):
            if start > prices[i]:
                start = prices[i]

            profit = max(profit, prices[i] - start)

        return profit