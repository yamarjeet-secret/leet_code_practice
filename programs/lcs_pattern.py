class Solution:
    def lcshelper(self,s1,s2,n,m,memo):
        if n==0 or m==0:
            return 0
        if memo[n][m] != -1:
            return memo[n][m]
        if s1[n-1] == s2[m-1]:
            memo[n][m] = 1+self.lcshelper(s1,s2,n-1,m-1,memo)
            return memo[n][m]
        else:
            memo[n][m]= max(self.lcshelper(s1,s2,n-1,m,memo),self.lcshelper(s1,s2,n,m-1,memo))
            return memo[n][m]
            
    def lcswithmemo(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        memo = [[-1]*(m+1) for _ in range(n+1)]
        return self.lcshelper(s1,s2,n,m,memo)
    
    def lcs(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
    
    def longestCommonSubstr(self, s1, s2):
        # code here
        n=len(s1)
        m=len(s2)
        value = 0
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    value = max(value, dp[i][j])
                else:
                    dp[i][j] =0
        return value
    

    def printlcs(self,s1,s2):
        n = len(s1)
        m = len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        i=n
        j=m
        ans = ''
        while i>0 and j>0:
            # if matched then diagonal value se mila ye
            if s1[i-1]==s2[j-1]:
                ans += s1[i-1]
                i = i-1
                j = j-1
            #otherwise jo max hota tha uske side jate the
            elif dp[i-1][j]>dp[i][j-1]:
                i = i-1
            else:
                j = j-1

        lcs = ans[::-1]

        return lcs
    
    def shortestCommonSupersequence(self, s1, s2):
         #code here
         n = len(s1)
         m = len(s2)
         dp = [[0]*(m+1) for _ in range(n+1)]
         for i in range(1,n+1):
             for j in range(1,m+1):
                 if s1[i-1]==s2[j-1]:
                     dp[i][j] = 1+ dp[i-1][j-1]
                 else:
                     dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
         lcs = dp[n][m]
        
         return n+m-lcs
    
    def minOperationsofdeleteandinsertion(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        lcs = dp[n][m]
        #logic no of deletion = len(s1)-lcs
        # no of insertion = len(s2)-lcs 
        # so total no of operation is n+m-2*lcs
        return n+m-2*lcs
    
    def longestPalinSubseq(self, s1):
        # code here
        s2 = s1[::-1]
        n = len(s1)
        m = len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
    
    def minDeletions(self, s1):
        # code here
        s2 = s1[::-1]
        n = len(s1)
        m = len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        lcs = dp[n][m]
        return n-lcs
    
    def LongestRepeatingSubsequence(self, s1):
		# Code here
        s2 = s1
        n = len(s1)
        m = len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1] and i!=j:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
    

    def isSubSeq(self, s1, s2):
        # code here
        i = 0  # pointer for s
        j = 0  # pointer for t
    
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1  # move pointer for s
            j += 1  # always move pointer for t
    
        return i == len(s1)

obj = Solution()
print(obj.printlcs("ABCDGH","AEDFHR"))


    
    

        