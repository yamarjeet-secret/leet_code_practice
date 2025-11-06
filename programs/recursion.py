
from typing import List,Optional
# n = (int(input()))

# sum1s = 0
# fst = input()
# l = fst.split(' ')
# for ele in l:
#     sum1s= sum1s+ int(ele)
# sum = n*(n+1)/2

# missingno = sum-sum1s

# print(int(missingno))


#repetition character

# t = input()
#ch = t[0]
n = 1
f = 1
def repetition_character(t):
    for i in t:
        if ch == i:
            n = n+1
            f = max(n,f)
        else:
            ch = i
            n = 1
    return f



# #minium moves
# n = (int(input()))

# sum1s = 0
# fst = input()
# l = fst.split(' ')
lst = []
# for ele in l:
#     lst.append(int(ele))
count = 0
def minimum_moves(n):
    for i in range(1, n):
        if lst[i]<lst[i-1]:
            count = count + (lst[i-1]-lst[i])
            lst[i] = lst[i-1]
    return count
# print(count)


#number spiral
# n = (int(input()))
# for i in range(0,n):
#     fst = input()
#     l = fst.split(' ')
#     x = (int(l[0]))
#     y = (int(l[1]))
#     # nub = number_function(x,y)
#     # print(nub)
#     if x<y:
#         if y%2==1:
#            nub = (y*y-x+1)
#            print(nub)
#         else:
#             nub = ((y-1)*(y-1)+x)
#             print(nub)
#     else:
#         if x%2==0:
#            nub = (x*x-y+1)
#            print(nub)
#         else:
#             nub = ((x-1)*(x-1)+y)
#             print(nub)
    
def spiral_number(x,y):
    if x<y:
        if y%2==1:
           nub = (y*y-x+1)
           return nub
        else:
            nub = ((y-1)*(y-1)+x)
            return nub
    else:
        if x%2==0:
           nub = (x*x-y+1)
           return nub
        else:
            nub = ((x-1)*(x-1)+y)
            return nub


# two knights
def calculatenumberofposition(n,i,j):
    
    flag = 0
    # if i==1 and j==1:
    #     return 0
    if(i-1>=0 and j-2>=0):
        flag=flag+1
    if(i+1<n and j-2>=0):
        flag=flag+1
    if( i+2<n and j-1>=0):
        flag=flag+1
    if(i+2<n and j+1<n):
        flag=flag+1
    if(i+1<n and j+2<n):
        flag=flag+1
    if(i-1>=0 and j+2<n):
        flag=flag+1
    if(i-2>=0 and j+1<n):
        flag=flag+1
    if( i-2>=0 and j-1>=0):
        flag=flag+1
        
    return n*n-flag-1

# n = int(input())
# arr = [[0]*n]*n
# # pos = 0
def calculate(n):
    pos = 0
    for i in range(0,n):
        for j in range(0,n):
            pos = calculatenumberofposition(n,i,j) + pos

    return pos/2


# for p in range(1,n+1):
#     x = int(calculate(p))
#     print(x)

# n = int(input())
# for p in range(1,n+1):
#     x = (p*p)*(p*p-1)/2
#     z = 4*(p-2)*(p-1)
#     print(int(x-z))


# permutation
# n = int(input())

def permutations(n):
    
    if (n==1):
        print('1')
    if (n==2 or n==3):
        print("NO SOLUTION")
    if(n>3):
        for i in range(2,n+1,2):
            print(i,end=' ')
        for i in range(1,n+1,2):
            print(i,end=' ')

# n = int(input())

# sum = n*(n+1)/2

# if sum%2==1:
#     print("NO")
# else:
#     print("YES")
#     for i in range(1,sum/2+1):
#         pass
    
    
    
# balance parenthesis
# s = input()
# #s = "((()))()()"
r = []
# flag = True

def balance_parenthesis(s):
    for st in s:
        if not st.isalpha():
            if(st == '(' or st == '{' or st == '['):
                r.append(st)
            if(st == ')'):
                if(r and (r[-1] == '[' or r[-1] == '{')):
                    return False
                if not r:
                    return False
                while(r and not r[-1]=='('):
                    r.pop()
                if r:
                    r.pop()

            if(st == '}'):
                if(r and (r[-1] == '[' or r[-1] == '(')):
                    return False
                if not r:
                    return False
                while(r and not r[-1]=='{'):
                    r.pop()
                if r:
                    r.pop()
            
            if(st == ']'):
                if(r and (r[-1] == '{' or r[-1] == '(')):
                    return False
                if not r:
                    return False
                while(r and not r[-1]=='['):
                    r.pop()
                if r:
                    r.pop()

    if not r:
        return True
    else:
        return False
    
    
# second approach

def isEqual( c1, c2) -> bool:
        if(c1 == '(' and c2 == ')'):
            return True
        if(c1 == '[' and c2 == ']'):
            return True
        if(c1 == '{' and c2 == '}'):
            return True
        return False

def isValid( s: str) -> bool:
    st = []
    for character in s:
        if(len(st) != 0):
            li = st[-1]
            if(isEqual(li, character)):
                st.pop()
                continue
        st.append(character)
    return len(st) == 0

# x = balance_parenthesis(s)

# print(x)




# n = (int(input()))

# fst = input()
# l = fst.split(' ')
# lst = []
# for ele in l:
#     lst.append(int(ele))
# stck = []
# stck.append(-1)

def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0]*n
        stck = []
        for i in range(n-1,-1,-1):
            count = 0
            while stck and heights[i]>stck[-1]:
                stck.pop()
                count += 1
            if stck:
                count += 1
            ans[i] = count
            stck.append(heights[i])
        return ans

def next_greater_element(lst):
    stck = []
    result = [-1]*len(lst)
    
    for i in range(len(lst)-1,-1,-1):
        while stck and lst[i]>=stck[-1]:
            stck.pop()
        if stck:
            result[i]= stck[-1]

        stck.append(lst[i])
    return result

# x = next_greater_element(lst)
# print(x)


def near_to_val(lst):
    stck = []
    
    for ele in lst:
        if stck and ele == stck[-1]:
            stck.pop()
        else:
            stck.append(ele)

    return stck

# y = near_to_val(lst)

# print(y)

def coin_piles(a,b):
    if max(a,b)>2*min(a,b):
        return "NO"
    if (a+b)%3 ==0:
        return "YES"
    else:
        return "NO"
# n = int(input())
# ans = []
# for i in range(0,n):
#     fst = input()
#     l = fst.split(' ')
#     lst = []
#     for ele in l:
#         lst.append(int(ele))

#     x = coin_piles(lst[0],lst[1])
#     print(x)
# print(lst)
# for i in range(0,len(lst)-1):
#     x = coin_piles(lst[i],lst[i+1])
#     print(x)

def trails_zero(n):
    ans = 0
    while(not n==0):
        # n = n%5
        #if(n%5==0):
        r = n//5
        ans = r + ans
        n = n//5

from collections import defaultdict

def palindrome_reorder(st):
    hmap = defaultdict(int)
    for i in range(len(st)):
        hmap[st[i]] += 1
    oddCount = 0

    for x in hmap:
        if (hmap[x] % 2 != 0):
            oddCount += 1
            oddChar = x
 
    # odd_cnt = 1 only if the length of
    # str is odd
    if (oddCount > 1 or oddCount == 1 and
            len(st) % 2 == 0):
        return "NO SOLUTION"
 
    # Generate first half of palindrome
    firstHalf = ""
    secondHalf = ""
 
    for x in sorted(hmap.keys()):
 
        # Build a string of floor(count/2)
        # occurrences of current character
        s = (hmap[x] // 2) * x
 
        # Attach the built string to end of
        # and begin of second half
        firstHalf = firstHalf + s
        secondHalf = s + secondHalf
 
    # Insert odd character if there
    # is any
    if (oddCount == 1):
        return (firstHalf + oddChar + secondHalf)
    else:
        return (firstHalf + secondHalf)
    
# st = input()
# ans = palindrome_reorder(st)
# print(ans)

#print(int(ans))



def gray_code(n):
    # Base case
    if (n <= 0):
        return ["0"]
    if (n == 1):
        return [ "0", "1" ]
 
    # Recursive case
    recAns = gray_code(n - 1)
 
    mainAns = []
     
    # Append 0 to the first half
    for i in range(len(recAns)):
        s = recAns[i]
        mainAns.append("0" + s)
 
    # Append 1 to the second half
    for i in range(len(recAns) - 1, -1, -1):
        s = recAns[i]
        mainAns.append("1" + s)
 
    return mainAns

def gray_code_withanothertechnique(output,n,arr):
    if n ==0:
        arr.append(output)
        return
    op1 = output+'0'
    op2 = output+'1'
    gray_code_withanothertechnique(op1,n-1,arr)
    gray_code_withanothertechnique(op2,n-1,arr)
    print(arr)
arr = []
# gray_code_withanothertechnique('',3,arr)


# n = int(input())
# gray_value = gray_code(n)
# for ele in gray_value:
#     print(ele)

def TowerOfHanoi(n , source_rod, dest_rod, helping_rod):
    if n == 1:
        print(source_rod, dest_rod)
        return
    TowerOfHanoi(n-1, source_rod, helping_rod, dest_rod)
    print(source_rod, dest_rod)
    TowerOfHanoi(n-1, helping_rod, dest_rod, source_rod)
    
# n = int(input())
# print(int(pow(2,n)-1))
# TowerOfHanoi(n,1,3,2)

outputs = set()
def permutations(input,op):
    if(len(input)==0):
        outputs.add(op)
        return
    op1 = op
    op2 = op
    op2 = op2+ input[0]
    input = input[1:]
    permutations(input,op1)
    permutations(input,op2)

# ip = "aabac"
# lst = permutations(ip,op='')
# print(outputs)

# s = sorted(ip)
# from itertools import permutations
# permutation = [''.join(p) for p in permutations(s)]
# # # Printing result
# print("Resultant List", len(permutation))
# for ele in permutation:
#     print(ele)


# s = input()
# # Convert s to list of input
# input = list(s)

# # Set to store possible strings
# outputs = set()

# Recursive function to create all possible permutations


def createstring(output, input):
    
    if len(input) == 1:
        outputs.add(output + input[0])
    else:
        for i in range(len(input)):
            createstring(output + input[i], input[0:i] + input[i+1:])


# We start with an empty output and all the characters of the strings as input
# createstring("", input)

# print(len(outputs))
# print("\n".join(sorted(outputs)))
outputs = list()

def targetsum(input_lst,vidx,target,output_lst):
    if(vidx==len(input_lst)):
        if target==0:
            outputs.append(output_lst)
            #print(output_lst)
            return
    if vidx<=len(input_lst)-1:
        targetsum(input_lst,vidx+1,target-input_lst[vidx],output_lst + " " + str(input_lst[vidx]))
        targetsum(input_lst,vidx+1,target,output_lst)

# n = int(input())
# sum = int(n*(n+1)/2)
# if not sum%2==0:
#     print("NO")
# else:
#     lst = []
#     for i in range(1, n+1):
#         lst.append(i)
#     # output_lst = list()
#     target = int(sum/2)
#     vidx =0
#     targetsum(lst,vidx,target,'')
#     list_temp = [outputs[0]]
#     list_1 = []
#     x = list_temp[0].split()
#     for ele in x:
#         list_1.append(int(ele))

#     list_2 = []
#     for ele in lst:
#         if ele not in list_1:
#             list_2.append(ele)
#     print("YES")
#     for ele in list_1:
#         print(ele, end = " ")
#     print()
#     for ele in list_2:
#         print(ele, end = " ")
        
        
def printpaths(curr,end,ans):
    if(curr==end):
        print(ans)
        return
    if(curr>end):
        return
    for i in range(1,n+1):
        if(curr+i<=end):
            printpaths(curr+i,end,ans+str(i))
            
# printpaths(0,6,'')




def permutationFindLetterCase(inputs,output,op_list):
    if len(inputs)==0:
        #print(output)
        op_list.append(output)
        return
    
    if inputs[0].isalpha()==True:
        out1 = output
        out2 = output
        out1+=inputs[0].lower()
        out2 += inputs[0].upper()
        inputs = inputs[1:]
        permutationFindLetterCase(inputs,out1,op_list) 
        permutationFindLetterCase(inputs,out2,op_list)
    else:
        out1=output
        out1+=inputs[0]
        inputs=inputs[1:]
        permutationFindLetterCase(inputs,out1,op_list)

    return op_list
inputs="A1B2"
output=""
print(permutationFindLetterCase(inputs,output,op_list=[]))


def generate_balace_parenthesis(open , close , output,arr):
    if (open==0 and close == 0 ):
        arr.append(output)
        return

    if (open!=0):
        op1= output
        op1+="("
        generate_balace_parenthesis(open-1,close,op1,arr)
    
    if (close>open):
        op2=output
        op2=op2+")"
        generate_balace_parenthesis(open,close-1,op2,arr)
    print(arr)

open=3
close=3
output=""
arr=[]
#generate_balace_parenthesis(open,close,output,arr)


def binarymore1than0s(zeros,ones,n,output,arr):
    if (n==0):
        arr.append(output)
        return
    if ones==zeros:
        binarymore1than0s(zeros,ones+1,n-1,output+'1',arr)
    else:
        binarymore1than0s(zeros+1,ones,n-1,output+"0",arr)
        binarymore1than0s(zeros,ones+1,n-1,output+"1",arr)
        
    print(arr)
    
arr = []
#binarymore1than0s(0,0,3,"", arr)

def simplifyPath(A):
    st = []
    pat = A.split("/")
    for ele in pat:
        if len(st)>0 and ele == '..':
            st.pop()
        elif ele == "." or ele == "":
            continue
        else:
            st.append(ele)
    final_ans = " "
    while len(st)>0:
        if len(st)>0:
            if st[-1] == "..":
                st.pop()
                final_ans = "/"
            else:
                final_ans = "/" + st.pop() + final_ans
    return final_ans

x = simplifyPath("/home/")
print(f"current path {x}")


def generateSubsets(Input):
    def helper(Op, In):
        if(In == ""):
            print(Op)
            return
        Op2 = Op
        Op2 += In[0]
        In = In[1:]
        helper(Op, In)
        helper(Op2, In)
    
    helper("", Input)
    
    
def kthGrammar(n,k):
    if(n==0 or n==1):
        return 0
        
    mid = pow(2,n-1)/2

    if(k<=mid):
        return int(kthGrammar(n-1,k))
    else:
        return int(not kthGrammar(n-1,k-mid))
    
# print(kthGrammar(2,2))

#input and output method

def permutation(ip,op):
    if(len(ip)==0):
        print(op)
        return
    op1 = op
    out2 = op
    out2 = out2 + ip[0]
    ip = ip[1:]
    permutation(ip,op1)
    permutation(ip,out2)

#permutation("abc","")


def permutation_with_space(S):
        # code here
        res=[]
        def solve(ip,op):
            if len(ip)==0:
                res.append(op)
                return
            op1=op
            op2=op
            op1+=ip[0]
            op2+=' '+ip[0]
            ip=ip[1:]
            solve(ip,op1)
            solve(ip,op2)
        ip=S[1:]
        op=S[0]
        solve(ip,op)
        return sorted(res)

# print(permutation_with_space("ABC"))


def permutation_with_case(inp,op):
    if len(inp)==0:
        print(op)
        return
    op1=op
    op2=op
    op1=op1+inp[0]
    op2=op2+inp[0].upper()
    inp=inp[1:]
    permutation_with_case(inp,op1)
    permutation_with_case(inp,op2)
    return
inp="abc"
op=""
# permutation_with_case(inp,op)

def josephus(n, k):

    if (n == 1):
        return 1
    else:

        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        return (josephus(n - 1, k) + k-1) % n + 1
    
    
    
    
def printKpc(qns,ans,m,op_list):
    if len(qns) == 0:
        op_list.append(ans)
        return
    #23 initaily
    ch = qns[0] #2
    roq = qns[1:] #3
    matched = m[ch] # abc
    for i in range(0,len(matched)): # run three times
        cho = matched[i]
        printKpc(roq,ans+cho,m,op_list)

    return op_list

def letterCombinations(self, digits: str) -> List[str]:
    m = {}
    m['2'] = "abc"
    m['3'] = "def"
    m['4'] = "ghi"
    m['5'] = "jkl"
    m['6'] = "mno"
    m['7'] = "pqrs"
    m['8'] = "tuv"
    m['9'] = "wxyz"
    ans = ""
    #digits = 23

    return printKpc(digits, ans, m, op_list = [])

