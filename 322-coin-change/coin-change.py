class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        coins.sort()

        for i in range(1, amount+1):
            minn = float("inf")
            for coin in coins:
                if i-coin<0:
                    break
                minn = min(minn, dp[i-coin]+1)

            dp[i] = minn

        return dp[amount] if dp[amount]<float("inf") else -1