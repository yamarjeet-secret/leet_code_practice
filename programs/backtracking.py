from typing import List,Optional
class Solution:
    def solution(self,nums,ans,cur,index):
        if(index>len(nums)):
            return
        ans.append(cur[:])
        for i in range(index,len(nums)):
            if(nums[i] not in cur):
                cur.append(nums[i])
                self.solution(nums,ans,cur,i)
                cur.pop()
        return 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(nums,ans,cur,0)
        return ans
    
    
    
    def backtracking(self, ans, m, digits, combination, index):
        if(index > len(digits)):
            return
        if(len(combination) == len(digits)):
            ans.append(combination[:])
            return

        currentDigit = digits[index]
        curString = m[currentDigit]

        for i in range(len(curString)):
            self.backtracking(ans, m, digits, combination +
                              curString[i], index+1)

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if(len(digits) == 0):
            return ans

        m = {}

        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"

        self.backtracking(ans, m, digits, "", 0)

        return ans