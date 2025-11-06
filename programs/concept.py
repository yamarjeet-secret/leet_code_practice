s1 = "Helw"

s2 = "dnaKlfHelddof"


d ={}
for i in s1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

d2 = {}
for i in s2:
    if i in d2:
        d2[i] += 1
    else:
        d2[i] =1


c = 0
flag = True
for i in s1:
    if i in d2 and d2[i] == 0:
        print("not possible")
        flag = False
        break
    elif i in d2 and d2[i] !=0:
        d2[i] -= 1
    else:
        print("not possible")
        flag = False
        break

if flag:
    print("possible")


def factorial(n):
    sum = 1
    for i in range(n, 0, -1):
        sum = sum * i
    yield sum

def fibonacci(nterms):
    n1, n2 = 0, 1
    for i in range(nterms):
        yield n1
        nth = n1 + n2
        n1 = n2
        n2 = nth



import copy
# === operator
lst1 = [2,3,4,5,6,7]
lst2 = lst1
lst2[2] = 100

print("equaloperator ",lst1,lst2)


#shallow copy -> in shallow copy both are referring to different different memory objects 

lst2 = lst1.copy()
lst2[1] = 100000

print("checking shallow copy for single list",lst2,lst1)



# shallow copy for nested list
list1 = [[1,2,3,4],[5,6,7,8]]

list2 = list1.copy()
list2[1][2] = 58888

print("checking shallow copy for single list",list2,list1)

print('\n')

lst2 = copy.deepcopy(lst1)
lst2[1] = 100000

print("checking deep copy for single list",lst2,lst1)

#deepcopy copy for nested list
list1 = [[1,2,3,4],[5,6,7,8]]

list2 = copy.deepcopy(list1)
list2[1][2] = 58888

print("checking deep copy for single list",list2,list1)

# decorator just check for how to call and use

def greet(fx):
    def mfx(*args,**kwargs):
        print("welcome to the world for addition man")
        fx(*args,**kwargs)
        print("thank your for using this data thanky so much binod")

    return mfx


@greet
def add(a,b):
    print(a+b)

add(2,3)


# generator in python are a special type of functions that 
# allow you to create an iterable sequence of values. A generator functions 
# returns a generator objects,which can be used to generate the valkue one by one
# Generators are useful when we want to produce a large sequence of values, but 
# we don't want to store all of them in memory at once.

def my_generator():
    for i in range(5):
        yield i
        
gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# threading things

import threading
from concurrent.futures import ThreadPoolExecutor
def func(times):
    print(f"sleeping the function for {times}")
    return times
    
    
t1 = threading.Thread(target=func,args=[2])
t2 = threading.Thread(target=func,args=[4])
t3 = threading.Thread(target=func,args=[3])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

def poolingdemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 4)
        # future3 = executor.submit(func, 2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l =[3,4,5,6]
        results = executor.map(func,l)
        for result in results:
            print(result)
#poolingdemo()

import multiprocessing
  
# empty list with global scope
result = []
  
def square_list(mylist):
    """
    function to square a given list
    """
    global result
    # append squares of mylist to global list result
    for num in mylist:
        result.append(num * num)
    # print global list result
    print("Result(in process p1): {}".format(result))
  
if __name__ == "__main__":
    # input list
    mylist = [1,2,3,4]
  
    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(mylist,))
    # starting process
    p1.start()
    # wait until process is finished
    p1.join()

    # print global result list
    print("Result(in main program): {}".format(result))
    


 


