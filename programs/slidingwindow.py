
def maximumSumSubarray(k,arr):
    i=0
    j=0
    csum=0
    maxi=0
    while j<len(arr):
        csum=csum+arr[j]
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            maxi=max(maxi,csum)
            csum=csum-arr[i]
            i+=1
            j+=1
    return maxi

k =3
arr = [1,2,3,4,5,6,7,8,9]

result = maximumSumSubarray(k,arr)
print(result)


def firstNegativeNumber(arr, n, k):
    i = 0
    j= 0
    neg_nums = []
    result = []
    
    #i till jpointer is less then n
    while j< n:
        #If we found negative then add it to neg num list
        if arr[j] < 0:
            neg_nums.append(arr[j])
        
        #increase jpointer till we did not reach window size    
        if((j- i + 1) < k):
            j+= 1
            
        #if window size
        elif ((j- i + 1) == k):
            #check that list of neg nums greater then 0 then add first element
            if len(neg_nums) > 0:
                result.append(neg_nums[0])
                #to remove all calc check first element with i pointer
                if arr[i] == neg_nums[0]:
                    neg_nums.pop(0)
                
            else:
                result.append(0)
                
            i += 1
            j+= 1
            
    return result
    
arr = [12, -1, -7, 8, -15, 30, 18, 28]
n = len(arr)
k = 3
ans = firstNegativeNumber(arr, n, k)
print(ans)



def anagram_count():

    # A Simple Python program to count anagrams of a
    # pattern in a text with the help of sliding window problem
    input = "forxxorfxdofr"
    ptr = "for"
    n = len(input)
    k = len(ptr)
    d = {}
    for i in ptr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1


    i = 0
    j = 0
    count = len(d)
    ans = 0

    while j < n:
        if input[j] in d:
            d[input[j]] -= 1
            if d[input[j]] == 0:
                count -= 1
        if (j-i+1) < k:
            j += 1
        elif (j-i+1) == k:
            if count == 0:
                ans += 1

            if input[i] in d:
                d[input[i]] += 1
                if d[input[i]] == 1:
                    count += 1

            i += 1
            j += 1
    print(ans)
    
    
    
def maximum_of_subarray_size_k(arr,k):
    i=j=0
    temp=[]
    result=[]
    n=len(arr)

    while j<n:
        if temp==[] or (temp[0]>=arr[j] and temp[-1]>=arr[j]):
            temp.append(arr[j])
        else:
            while temp!=[] and temp[-1]<arr[j]:
                temp.pop()
            temp.append(arr[j])
        if j-i+1==k:
            result.append(temp[0])
            if temp[0]==arr[i]:
                temp.pop(0)
            i+=1
        j+=1

    return result

k =3
arr = [1,2,3,4,5,6,7,8,9]
res = maximum_of_subarray_size_k(arr,k)
print("result is ",res)


# Python implementation to find the length
# of longest subarray having sum k

# function to find the length of longest
# subarray having sum k
import sys

def variable_size_window_given_sum(A, N, K):

	i, j, sum = 0, 0, 0
	maxLen = -sys.maxsize -1

	while (j < N):
		sum += A[j]
		if (sum < K):
			j += 1
		elif (sum == K):
			maxLen = max(maxLen, j - i + 1)
			j += 1
		elif (sum > K):
			while (sum > K):
				sum -= A[i]
				i += 1
			if (sum == K):
				maxLen = max(maxLen, j - i + 1)
			j += 1
	return maxLen

# Driver Code
arr = [ 10, 5, 2, 7, 1, 9 ]
n = len(arr)
k = 15
print("Length = "+ str(variable_size_window_given_sum(arr, n, k)))

def variable_size_window_given_sum_negative_no_also_present():
    arr = [5,3,-15,7,8,8,-9]
    s = 8
    max_lst, t = [], []
    i, j = 0, 0
    while j < len(arr)-1:
        if i < len(arr):
            t.append(arr[i])
            if sum(t) <= s:
                i += 1
            if sum(t) == s:
                if t not in max_lst:
                    max_lst.append(len(t)) 
            if sum(t) > s or i == len(arr) -1:
                t = []
                j += 1
                i = j
        else:
            i = 0
            t = []
    print(max(max_lst))


