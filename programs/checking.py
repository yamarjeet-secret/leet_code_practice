
 
# using naive method to get
# Maximum frequency character in String
test_str = ""
all_freq = {}
for i in test_str:
    print(i)
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
 
# printing result
print ("The maximum of all characters in GeeksforGeeks is : " + str(res))


def appendAndDelete(s, t, k):
    ns=len(s)
    nt=len(t)
    ne=0
    for i in range(min(ns,nt)):
        if s[i]!=t[i]:
            break
        ne=i+1
    d = k-(ns+nt-2*ne)
    return 'Yes' if d>=0 and (d%2 == 0 or d>2*ne) else 'No'

s = appendAndDelete(s='abc',t='abc',k =7)

print(s)

s= "Learning pythone is very easy"
l = s.split()
print(l)
i = len(l)-1
l1 = []
while i>=0:
    l1.append(l[i])
    i=i-1

output = ' '.join(l1)


print(output)

n = (int(input()))

# creating an empty list
lst = []
sum1s = 0
# iterating till the range
for i in range(1, n):
    ele = int(input())
    # adding the element
    lst.append(ele)
    sum1s= sum1s+ele
sum = n*(n+1)/2

    
missingno = sum-sum1s

print(int(missingno))


    
    
    
def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


print(length_of_longest_substring("abcdcae"))
    

