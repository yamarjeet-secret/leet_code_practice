def appartments():
    fst = input()
    lst = fst.split()
    k = int(lst[2])
    temp1 =[]
    fst1 = input()
    fst1 = fst1.split()
    temp1 = list(map(int,fst1))


    fst2 = input()
    fst2 = fst2.split()
    temp2 = list(map(int,fst2))
    temp1.sort()
    temp2.sort()

    # # temp1 = [90, 41, 20, 39, 49, 21, 35, 31, 74, 86]

    # # temp2 = [14, 24, 24, 7, 82, 85, 82, 4, 60, 95]

    # # k = 10
    j = 0
    count = 0
    for i in range(0, len(temp1)):
        for j in range(j,len(temp2)):
            if temp2[j]+k < temp1[i]:
                j+=1
            elif temp2[j]-k > temp1[i]:
                break
            else:
                j+=1
                count+=1
                break
    print(count)



def ferriswheel():
    n = input()
    lst = n.split()
    x = int(lst[1])
    list1 = input()
    list1 = list1.split()
    list1 = list(map(int,list1))
    list1.sort()
    list1 = list1[::-1]
    count = 0
    j = len(list1)-1
    i = 0
    while(i<=j):
        # if (list1[i] + list1[j])>x:
        #     j = j1
        if (list1[i] + list1[j])<=x:
            count +=1
            j -= 1
            i += 1
        else:
            count +=1
            i += 1
    print(count)

def concerttickets():
    n = input()
    k = n.split()
    r = int(k[1])
    ticket_price = input()
    ticket_price = ticket_price.split()
    ticket_price = list(map(int,ticket_price))
    customer_price = input()
    customer_price = customer_price.split()
    customer_price = list(map(int,customer_price))
    ticket_price.sort()
    
    j = len(ticket_price)-1
    for price in ticket_price:
        if price<=customer_price[j]:
            print(price,end = '')
            ticket_price.remove(price)
            
            
def restaurants():
    n = int(input())

    arrival = []
    leave = []

    for i in range(n):
        x, y = input().split()
        arrival.append(int(x))
        leave.append(int(y))

    arrival.sort()
    leave.sort()
    # n = 10
    # arrival = [1,2,3,4,5,6,7,8,9,10]
    # leave = [11,12,13,14,15,16,17,18,19,20]
    result = 0
    current = 0
    i , j = 0,0

    while i < n and j<n:
        if arrival[i] <= leave[j]:
            current +=1
            i += 1
        elif arrival[i]>leave[j]:
            current -=1
            j +=1

        result = max(current,result)


    print(result)
    



def movie_tickets():
    n = int(input())

    movies = []


    for i in range(n):
        x, y = map(int,input().split())
        movies.append((x,y))

    movies.sort(key=lambda x:x[1])

    end_time = 0
    count = 0
    for start,end in movies:
        if start>=end_time:
            count+=1
            end_time = end


    print(count)



def sumoftwovalues():
    n = input()
    k = n.split()
    sum_ex = int(k[1])
    arr = input()
    arr = arr.split()
    real_arr = list(map(int,arr))
    temp_arr = real_arr[:]
    temp_arr.sort()
    x = 0
    y = 0
    i = 0
    j = len(temp_arr)-1
    while(i<j):
        temp_sum = temp_arr[i]+temp_arr[j]
        if temp_sum==sum_ex:
            x = temp_arr[i]
            y = temp_arr[j]
            break
        elif temp_sum<sum_ex:
            i = i+1
        elif temp_sum>sum_ex:
            j = j-1
        else:
            i =i+1
            j =j-1
            
    if x==0 and y==0:
        print("IMPOSSIBLE")
    else:
        # for i in range(0,len(real_arr)-1):
        #     if x==real_arr[i]:
        #         index1 = i
        #     if y==real_arr[i]:
        #         index2 = i
        lst = list()
        index1,index2 = 0,0
        if x==y:
            for i in range(0,len(real_arr)):
                if real_arr[i] ==x:
                    lst.append(i)
                if len(lst)==2:
                    index1 = lst[0]
                    index2 = lst[1]
                    break
            
            print(index1+1, index2+1)
        else:
            index1 = real_arr.index(x)
            index2 = real_arr.index(y)
            
            if index2>index1:
                print(index1+1, index2+1)
            else:
                print(index2+1, index1+1)
    
    
from bisect import bisect_right

def binary_search(tickets, budget):
    
    left, right = 0, len(tickets) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if tickets[mid] <= budget:
            result = tickets[mid]
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def concerttickets():
    inp = input()
    k = inp.split()
    n = int(k[0])
    m = int(k[1])
    concert_price = input()
    concert_price = concert_price.split()
    concert_price = list(map(int,concert_price))
    concert_price.sort()
    user_price = input()
    user_price = user_price.split()
    user_price = list(map(int,user_price))
    # for ele in user_price:
    #     idx = bisect_right(concert_price,ele)
    #     #res = min(enumerate(concert_price), key=lambda x: abs(ele - x[1]))
    #     # concert_price.remove(res[1])
    #     if idx==0:
    #         print(-1)
    #     else:
    #         if concert_price:
    #             print(concert_price[idx-1])
    #             concert_price.pop(idx-1)
    #         else:
    #             print(-1)
    for budget in user_price:
        price = binary_search(concert_price,budget)
        #res = min(enumerate(concert_price), key=lambda x: abs(ele - x[1]))
        # concert_price.remove(res[1])
        if price!=-1:
            print(price)
            concert_price.remove(price)
        else:
            print(-1)



def median(lst):
    n = len(lst)
    lst.sort()
    if n%2==0:
        return (lst[n//2]+lst[n//2-1])/2
    else:
        return (lst[n//2])
    
def stsicklength():
    n = int(input())
    k = input()
    lst = list(map(int,k.split()))
    #lst = lst.sort()
    median_length = median(lst)
    total_cost = 0
    for ele in lst:
        total_cost += abs(ele-median_length)
    
    print(int(total_cost))
    
import sys
def kadanealgo():
    n = int(input())
    k = input()
    lst = list(map(int,k.split()))
    csum = 0
    maxsum = -sys.maxsize - 1
    for ele in lst:
        csum = csum + ele
        maxsum = max(csum,maxsum)
        if csum<0:
            csum = 0
    print(maxsum)
kadanealgo()



def missingcoinsum():
    n = int(input())
    a = sorted(list(map(int,input().split())))

    currSum = 0
    for i in range(n):
        if currSum + 1 < a[i]:
            break
        currSum += a[i]

    print(currSum+1)

def collectingnumber():
    # n = int(input())
    # a = (list(map(int,input().split())))
    # max_collect = a[0]
    # pos = [0]*(n+1)
    
    # for i in range(1,n+1):
    #     pos[a[i]] = i
    # count = 1
    # for i in range(1,n+1):
    #     if pos[i]>pos[i-1]:
    #         count += 1

    # print(count)
    
    n = int(input())
    a = (list(map(int,input().split())))
    next_element = [False] * 200001

    rounds = 0
    for i in range(n):
        val = a[i]
        if not next_element[val]:
            rounds += 1
        if val < n:
            next_element[val + 1] = True

    print(rounds)
collectingnumber()


def playlist():
    n = int(input())
    a = (list(map(int,input().split())))
    s = set()
    l,r =0,0
    overall_max= 0
    while r<n:
        if a[r] in s:
            s.remove(a[l])
            l +=1
        elif a[r] not in s:
            s.add(a[r])
            r +=1
            overall_max = max(r-l,overall_max)

    print(overall_max)
playlist()
