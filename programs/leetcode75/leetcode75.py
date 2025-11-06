from typing import List
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """_summary_

        Args:
            word1 (str): _description_
            word2 (str): _description_
        word1 = "abc"
        word2 = "pqr"
        o/p = "apbqcr"
        Returns:
            str: _description_
        """
        l1=len(word1)
        l2 = len(word2)
        flag = True
        i = 0
        j = 0
        res = ''
        while(i<l1 and j<l2):
            if flag:
                res=res+word1[i]
                i = i+1
            else:
                res = res+word2[j]
                j = j+1
            flag = not flag
        
        while(i<l1):
            res=res+word1[i]
            i = i+1
        while(j<l2):
            res=res+word2[j]
            j = j+1
        return res


    """ 
            Example 1:

    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"
    Example 2:

    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"
    Example 3:

    Input: str1 = "LEET", str2 = "CODE"
    Output: ""
    """
    def gcdofnum(self,a,b):
        while(not a%b == 0):
            rem = a%b
            a = b
            b = rem
        return b
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(str1+str2 == str2+str1):
            ans = self.gcdofnum(len(str1),len(str2))
            return str1[0:ans]
        else:
            return ""
        

    """
        Input: flowerbed = [1,0,0,0,1], n = 1
        Output: true 
    """
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(0,len(flowerbed)):
            if(flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i == len(flowerbed)-1 or flowerbed[i+1] ==0 )):
                count = count+1
                flowerbed[i] = 1
                if count>=n:
                    break
        if count>=n:
            return True
        else:
            return False
 

    def isvowels(self,s):
        if s == 'a' or s == 'A' or s == 'e' or s == 'E'  or s == 'i' or s == 'I' or s == 'o' or s == 'O' or s == 'u' or s == 'U':
            return True
        else:
            return False

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i =0
        j = len(s)-1
        res = ""
        while(i<j):
            if self.isvowels(s[i]) and self.isvowels(s[j]):
                s[i], s[j] = s[j], s[i]
                i =i+1
                j =j-1
            elif not self.isvowels(s[i]):
                i =i+1
            elif not self.isvowels(s[j]):
                j =j-1
        for ele in s:
            res = res + ele
        return res
    
    def reverseWords(self, s: str) -> str:
        res=s.split()[::-1]
        ans = " ".join(res)
        return ans


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = 1
        suffix[n-1] = 1
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suffix[j] = suffix[j+1]*nums[j+1]
        ans = [0]*n
        for i in range(n):
            ans[i] = prefix[i]*suffix[i]
        return ans
    
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        """ first < second< ele """
        first,second = 5555555555555,55555555555
        temp = [0]*3
        tmp = []
        for ele in nums:
            if ele<=first:
                first = ele
                temp[0] = first
            elif ele<=second:
                second = ele
                temp[1] = second
            else:
                temp[2] = ele
                return True
        return False
    
    def compress(self, chars: List[str]) -> int:
        ans = ""
        count =1
        ans = ans + chars[0]
        i =1
        while i<len(chars):
            if chars[i]==chars[i-1]:
                count+=1
            else:
                if count>1:
                    ans = ans + str(count)
                ans=ans+str(chars[i])
                count = 1
            i = i+1
        if count>1:
            ans = ans+str(count)
        for ele in range(0,len(ans)):
            chars[ele]=ans[ele]
        del chars[len(ans):]
        return len(chars)
    
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        while i< len(nums) and j<len(nums):
            if nums[i]==0 and nums[j]==0:
                j = j+1
            elif nums[i]==0 and (nums[j]>0 or nums[j]<0):
                nums[i],nums[j] = nums[j],nums[i]
                i = i+1
                j = j+1
            elif (nums[i]>0 or nums[i]<0) and nums[j]==0:
                    i = i+1
                    j = j+1
            elif (nums[i]>0 or nums[i]<0) and (nums[j]>0 or nums[j]<0):
                    i = i+1
                    j = j+1
            
        return nums
    
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m= len(t)
        i = 0
        j=0
        count=0
        while i<n and j<m:
            if s[i]==t[j]:
                i = i+1
                j= j+1
                count = count+1
            else:
                j= j+1
        if count==n:
            return True
        else:
            return False
        
    def conatinerWithWater(self, height: List[int]) -> int:
        """find the conatiner that contain most water

        Args:
            height (List[int]): height = [1,8,6,2,5,4,8,3,7]

        Returns:
            int: _description
        """
        start = 0
        end = len(height)-1
        maxarea = 0
        while(start<end):
            area = (min(height[start],height[end]))*(end-start)
            maxarea = max(area,maxarea)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return maxarea
    
    
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        start = 0
        end = len(nums)-1
        while start<end:
            if nums[start]+nums[end]<k:
                start+=1
            elif nums[start]+nums[end]>k:
                end-=1
            else:
                start+=1
                end-=1
                ans+=1
        
        return ans
    
    

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        maxavg = 0
        csum=0
        while j<len(nums):
            csum += nums[j] 
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                avg = csum/k
                maxavg = max(avg,maxavg)
                csum = csum-nums[i]
                i+=1
                j+=1
        return maxavg


    def maxVowels(self, s: str, k: int) -> int:
        i =0
        j=0
        maxcount = 0
        cstr = ""
        ccount = 0
        while j<len(s):
            cstr+= s[j]
            if s[j] in 'aeiou':
                ccount+=1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                maxcount = max(maxcount,ccount)
                if cstr[0] in 'aeiou':
                    ccount-=1
                cstr = cstr[1:]
                i+=1
                j+=1
        return maxcount
    
    def variable_size_window_given_sum(self, nums, K):

        i, j, N = 0, 0, len(nums)
        maxLen = 0
        count =0
        while (j < N):
            if nums[j]==1:
                count+=1
            if (count < K):
                j += 1
            if (count == K):
                maxLen = max(maxLen, j - i + 1)
                j += 1
            elif (count > K):
                while (count > K):
                    count -= 1
                    i += 1
                if (count == K):
                    maxLen = max(maxLen, j - i + 1)
                j += 1
        return maxLen
    
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j, N = 0, 0, len(nums)
        for j in range(N):
            if nums[j]==0:
                k-=1
            if k<0:
                if nums[i]==0:
                    k+=1
                i+=1
        return j-i+1


x = Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)
print(x)