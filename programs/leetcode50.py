'''
https://github.com/BitPunchZ/Leetcode-in-python-50-Algorithms-Coding-Interview-Questions/tree/master
'''


from typing import List,Optional
import math
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #second approach
        zero_index = 0
        for non_zero_index in range(0,len(nums)):
            if (nums[non_zero_index]!=0):
                nums[zero_index] = nums[non_zero_index]
                zero_index+=1
        for i in range(zero_index,len(nums)):
            nums[i] = 0
        return nums
    
    def ContainerWithMostWaterMaxArea(self, height: List[int]) -> int:
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
    
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        s = 0
        end =  len(people)-1
        boats = 0
        while s<=end:
            if people[s]+people[end] <= limit:
                boats+=1
                end -=1
                s+=1
            else:
                boats +=1
                end-=1
        return boats
    
    def validMountainArray(self, arr: List[int]) -> bool:
        """strictly decreasing and increasing the array

        Args:
            arr (List[int]): _description_

        Returns:
            bool: _description_
        """
        i=1
        while(i<len(arr) and arr[i]>arr[i-1]):
            i+=1

        if(i==1 or i==len(arr)):
            return False

        while(i<len(arr) and arr[i]<arr[i-1]):
            i+=1
        return i==len(arr)
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        while(left<n and right<n):
            el = s[right]
            if(el in m):
                left = max(left,m[el]+1)
            m[el] = right
            ans = max(ans,right-left+1)
            right+=1
        return ans
    
    
    def getLeftPosition(self, nums, target):
        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = left+(right-left)//2
            if(nums[mid] == target):
                if(mid-1 >= 0 and nums[mid-1] != target or mid == 0):
                    return mid
                right = mid-1
            elif(nums[mid] > target):
                right = mid-1
            else:
                left = mid+1

        return -1

    def getRightPosition(self, nums, target):
        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = left+(right-left)//2
            if(nums[mid] == target):
                if(mid+1 < len(nums) and nums[mid+1] != target or mid == len(nums)-1):
                    return mid
                left = mid+1
            elif(nums[mid] > target):
                right = mid-1
            else:
                left = mid+1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)

        return [left, right]
    
    
    def countPrimes(self, n: int) -> int:		
        
        if n<2:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2,math.ceil(math.sqrt(n))):
            if isPrime[i]:
                for multiples_of_i in range(i*i,n,i):
                    isPrime[multiples_of_i] = False
        
        return sum(isPrime)
    
    
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)
    
    def addBinary(self, a, b):
        result = []
        carry = 0
        i = len(a)-1
        j = len(b)-1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total//2

        return ''.join(reversed(result))
    
    
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = m.get(num,0)+1
        for num in nums:
            if(m[num]>len(nums)//2):
                return num
            
    def majorityElementsecondapproach(self, nums: List[int]) -> int:
        count = 1
        majority = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == majority:
                count+=1
            else:
                count -= 1
                if count == 0:
                    majority = nums[i]
                    count = 1
        return majority
    
    def findHash(self,s):
        return ''.join(sorted(s))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        m = {}

        for s in strs:
            hashed = self.findHash(s)
            if(hashed not in m):
                m[hashed] = []
            m[hashed].append(s)
        
        for p in m.values():
            answers.append(p)
        
        return answers
    
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
      m = {}
      ans = 0

      for i in range(0,len(A)):
        x = A[i]
        for j in range(0,len(B)):
          y = B[j]
          if(x+y not in m):
            m[x+y] = 0
          m[x+y]+=1

      for i in range(0,len(C)):
        x = C[i]
        for j in range(0,len(D)):
          y = D[j]
          target = -(x+y)
          if(target in m):
            ans+=m[target]

      return ans
  
  
  
  
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)

        if(len1 < len2):
            return ""

        hashPat = {}
        hashStr = {}

        for i in range(0, len2):
            if(hashPat.get(t[i]) is None):
                hashPat[t[i]] = 0
            hashPat[t[i]] += 1

        count = 0
        left = 0
        startIndex = -1
        minLen = float("inf")

        for right in range(0, len1):

            if(hashStr.get(s[right]) is None):
                hashStr[s[right]] = 0
            hashStr[s[right]] += 1
            if(hashPat.get(s[right]) is None):
                hashPat[s[right]] = 0
            if (

                hashPat.get(s[right]) != 0 and
                hashStr.get(s[right]) <= hashPat.get(s[right])
            ):
                count += 1  # keep incrementing the count if string hash is less then pattern hash
            # count==len2 means a window is found that contains all character of pattern string
            if (count == len2):

                if(hashStr.get(s[left]) is None):
                    hashStr[s[right]] = 0
                if(hashPat.get(s[left]) is None):
                    hashPat[s[right]] = 0
                while (
                    hashStr.get(s[left]) > hashPat.get(s[left]) or
                    hashPat.get(s[left]) == 0
                ):
                    #minimizing the windows range from left side

                    if (hashStr.get(s[left]) > hashPat.get(s[left])):
                        hashStr[s[left]] -= 1
                    left += 1  # incrementing the left pointer

                windowLen = right - left + 1  # calculating the windows length
                if (minLen > windowLen):
                    minLen = windowLen
                    startIndex = left

        if (startIndex == -1):
            return ""
        return s[startIndex:startIndex+minLen]
    
    
    
    
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        ans = cur
		
        while(l1 and l2):
            if(l1.val>l2.val):
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
            
        if(l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        if(l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return ans.next
    
    def hasCycle(self, head: ListNode) -> bool:
        hare = head
        turtle = head

        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if(turtle == hare):
                return True
        return False
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None:
            cn = current.next
            
            current.next = prev
            prev = current 
            current = cn
            
        head = prev
        
        return head
    
    def rotatebyK(self, head, k):
        # code here
        tail = head
        prev = None
        while tail.next:
            tail = tail.next
        while k>0:
            prev = head
            head = head.next
            prev.next = None
            
            tail.next = prev
            tail = prev
            prev = head
            k = k-1
            
        return head
    
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(None)
        pointer = ans

        carry = 0
        sum = 0

        while(l1!=None or l2!=None):
            sum = carry
            if(l1!=None):
                sum+=l1.val
                l1 = l1.next
            if(l2!=None):
                sum+=l2.val
                l2 = l2.next
            
            carry = int(sum/10)
            pointer.next  = ListNode(sum%10)

            pointer = pointer.next
        
        if(carry>0):
            pointer.next = ListNode(carry)
        
        return ans.next
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
    
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(not head):
            return head

        odd = head
        even = odd.next
        evenList = even

        while(even and even.next):
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenList
        return head
    
    def mergeTwoLists(self, l1, l2):
        cur = ListNode(0)
        ans = cur

        while(l1 and l2):
            if(l1.val > l2.val):
                cur.next = l2
                l2 = l2.next

            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        while(l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while(l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return ans.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if(len(lists) == 0):
            return None

        i = 0
        last = len(lists)-1
        j = last

        while(last != 0):
            i = 0
            j = last

            while(j > i):
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j

        return lists[0]