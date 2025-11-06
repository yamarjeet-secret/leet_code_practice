class Solution(object):

    def climbStairs(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        return self.climbStairs(n-1)+ self.climbStairs(n-2)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[1],dp[0] = 1,1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
    
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n = len(cost)
    
        if n == 1:
            return cost[0]
        
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        # Return minimum of cost to 
        # climb (n-1)th stair and 
        # cost to reach (n-2)th stair
        return min(dp[n - 1], dp[n - 2])
    
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
    
        # dp[i] = min cost to reach step i
        dp = [0] * (n + 1)
        
        # Base cases: starting at step 0 or step 1
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])
        
        return dp[n]
    
    def maxGold(self, mine):
        # code here
        n = len(mine)
        m = len(mine[0])
        for col in range(m - 1, -1, -1):
            for row in range(n):
                if col == m-1:
                    pass
                elif row == 0:
                    mine[row][col]+=max(mine[row][col + 1], mine[row + 1][col + 1])    
                elif row == n - 1:
                    mine[row][col]+=max(mine[row][col+1], mine[row-1][col+1]) 
                else:    
                    mine[row][col]+=max(mine[row][col+1], mine[row-1][col+1], mine[row+1][col+1])
        
        answer = 0
        for i in range(n):        
            answer = max(answer, mine[i][0])
        return answer
    

    def minimumCostPath(self, grid):
		#Code here
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n - 1 and j == m - 1:
                    dp[i][j] = grid[i][j]
                elif i == n - 1:
                    dp[i][j] = dp[i][j + 1] + grid[i][j]
                elif j == m - 1:
                    dp[i][j] = dp[i + 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        return dp[0][0]
    


    def num_decodings(digits: str) -> int:
        if not digits or digits[0] == '0':
            return 0

        n = len(digits)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string
        dp[1] = 1  # first digit (already checked it's not '0')

        for i in range(2, n + 1):
            one_digit = int(digits[i-1])
            two_digits = int(digits[i-2:i])

            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[n]