#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        n = len(price)
        lengths = [i + 1 for i in range(n)] 
        # for memoized the recursive call
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if lengths[i - 1] <= j:
                    dp[i][j] = max(price[i - 1] + dp[i][j - lengths[i - 1]], 
                                   dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][n]
    
    def cutRodoptimised(self, price):
        #code here
        n = len(price)
        dp = [0] * (n + 1)
    
        for i in range(1, n + 1):  # i = current rod length
            for j in range(i, n + 1):  # j = total rod length we're solving for
                dp[j] = max(dp[j], price[i - 1] + dp[j - i])
    
        return dp[n]
    

    def countcoinChange(self, coins, sum):
        # code here 
        n = len(coins)
        # for memoized the recursive call
        dp = [[0] * (sum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(sum + 1):
                if i==0:
                    dp[i][0] = 0
                if j == 0:
                    dp[0][j]=1
                if coins[i - 1] <= j:
                    dp[i][j] = (dp[i][j - coins[i - 1]] + dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][sum]
    
    def minCoins(self, coins, target):
        # code here
        INF = float('inf')
        dp = [INF] * (target + 1)
        dp[0] = 0  # Base case: 0 coins needed for sum 0

        for coin in coins:
            for amt in range(coin, target + 1):
                if dp[amt - coin] != INF:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)

        return dp[target] if dp[target] != INF else -1
    
