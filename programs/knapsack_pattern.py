class Solution:


    def knapsack(self, W, val, wt):
        # code here
        n = len(wt)
        # for memoized the recursive call
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if wt[i - 1] <= j:
                    dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], 
                                   dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][W]


    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        dp = [[False] * (sum + 1) for _ in range(n + 1)]
        for i in range(n+1):
            for j in range(sum+1):
                if i==0:
                    dp[i][0] = False
                if j ==0:
                    dp[0][j] = True
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]  # Can't include the current number
                else:
                    # Either include arr[i-1] or don't
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                    
        return dp[n][sum]
        
    def equalPartition(self, arr):
        # code here
        calsum = sum(arr)
        if calsum %2 !=0:
            return False
        else:
            return self.isSubsetSum(arr, calsum//2)
        

    def perfectSum(self, arr, target):
        #  means count of susbset of a given sum
        n = len(arr)
        dp = [[0]*(target+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(target+1):
                # means empty array subset and expecting a target so it is not valid
                # thats why here put 0
                if i==0:
                    dp[i][0] = 0
                # means empty array subset we can opt for sum=0 i.e put 1
                if j==0:
                    dp[0][j] = 1
                if arr[i-1]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
                    
        return dp[n][target]
    
    def countPartitionswithgivendifference(self, arr, d):
        # code here
        calsum = sum(arr)
        target = (d+calsum)//2
        if (calsum + d) % 2 != 0:
            return 0
        #print(target)
        return self.perfectSum(arr,target)
    
    def findTargetSumWays(self, n, arr, target):
        # code here (+,- sign given here)
        
        calsum = sum(arr)
        target_sum = (calsum + target)//2
        #print(target_sum)
        if (calsum + target) % 2 != 0 or calsum < abs(target):
            return 0
        else:
            return self.perfectSum(arr,target_sum)