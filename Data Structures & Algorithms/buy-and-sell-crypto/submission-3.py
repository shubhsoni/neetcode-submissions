class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy
        ans = 0

        for i,p in enumerate(prices):
            if i == 0:
                buy = p
                continue
            if p - buy < 0:
                buy = p
                profit = 0 #reset profit
            else:
                profit = p - buy
                ans = max(ans, profit)

        return ans

        