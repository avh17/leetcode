class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i, n):
            if i>=len(coins) or n<=0:
                return 1 if n==0 else 0

            return dp(i, n-coins[i])+dp(i+1, n)

        return dp(0, amount)