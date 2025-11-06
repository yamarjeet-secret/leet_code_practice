n = int(input())
fst = input()
lst = fst.split()
temp =[]
for ele in lst:
    temp.append(int(ele))

#arr = [[0]*cols]*rows
import sys
temp = [238, 224 ,861, 461, 558, 860, 318, 93, 347, 402]

# A Recursive Python3 program to solve
# minimum sum partition problem.
import sys

# Returns the minimum value of the
# difference of the two sets.


def minimumsubsetsumdifference(lst,n,target):
    su = sum(lst)
    dp = [[0 for i in range(target + 1)]
		for j in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = True
    for j in range(1,target+1):
        dp[0][j] = False
    
    for i in range(1,n+1):
        for j in range(1,target+1):
            if lst[i-1]<=j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-lst[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    diff = sys.maxsize
    for j in range(su//2, -1 ,-1):
        if dp[n][j]==True:
            diff = su-(2*j)
            break
    return diff


# Driver code
n = len(temp)

# print(findMinSubsetsumdifferenc(temp, n))

# This code is contributed by Tokir Manva

def targetsum(lst,n,target):

    dp = [[0 for i in range(target + 1)]
		for j in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = True
    for j in range(1,target+1):
        dp[0][j] = False
    
    for i in range(1,n+1):
        for j in range(1,target+1):
            if lst[i-1]<=j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-lst[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]

target = sum(temp)
x = targetsum(temp,n,target)
print(x)



def count_rotated_array(A):
    n = len(A)
    if n == 1:
        return 0
    if A[0] < A[-1]:
        return 0

    start = 0
    end = n - 1

    while (start <= end):
        mid = start + int((end-start)/2)

        prev = (mid-1 + n) % n
        if A[mid] <= A[prev]:
            # return n - mid if array is left rotated
            return mid
        if A[mid] <= A[end] and A[start] <= A[mid]:
            return start
        elif A[start] <= A[mid]:
            start = mid + 1
        elif A[mid] <= A[end]:
            end = mid - 1
    return 0