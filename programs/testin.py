
# from typing import List,Optional
# def lengthOfLongestSubstring(s: str) -> int:
#     d = {}
#     l = 0
#     r = 0
#     n = len(s)
#     longest = 0
#     while l<n and r <n:
#         current_char = s[r]
#         if current_char in d:
#             prev_char = d[current_char]
#             l = max(l,prev_char+1)
#         d[current_char] = r
#         longest = max(longest,r-l+1)
#         r += 1
            
#     return longest

# # print(lengthOfLongestSubstring("abcdcae"))
# def printss(ques,ans):
#     if len(ques) == 0:
#         print(ans)
#         return
#     ch = ques[0]
#     roq = ques[1:]
#     printss(roq,ans+ch)
#     printss(roq,ans+"")

# # print(printss('yvta',''))






# def printKpc(qns,ans,m,op_list):
#     if len(qns) == 0:
#         op_list.append(ans)
#         return
#     #23 initaily
#     ch = qns[0] #2
#     roq = qns[1:] #3
#     matched = m[ch] # abc
#     for i in range(0,len(matched)): # run three times
#         cho = matched[i]
#         printKpc(roq,ans+cho,m,op_list)

#     return op_list


# def letterCombinations(digits: str) -> List[str]:
#     m = {}
#     m['2'] = "abc"
#     m['3'] = "def"
#     m['4'] = "ghi"
#     m['5'] = "jkl"
#     m['6'] = "mno"
#     m['7'] = "pqrs"
#     m['8'] = "tuv"
#     m['9'] = "wxyz"
#     ans = ""
#     #digits = 23

#     return printKpc(digits, ans, m, op_list = [])

# # z = letterCombinations("678")
# # print(z)



# def printperm(ques,ans):
#     if len(ques)==0:
#         print(ans)
#         return
#     for i in range(0,len(ques)):
#         ch = ques[0]
#         roq = ques[0:i] + ques[i+1:]
#         #print(roq)
#         printperm(roq, ans+ch)
    
# printperm("abc","")



# def count_encodings_recursive(ques, ans=""):
#     if not ques:  # Base case: empty string means an encoding is complete
#         print(ans)
#         return

#     # Option 1: Encode the first single digit
#     first_digit = int(ques[0])
#     if 1 <= first_digit <= 9:
#         char_one_digit = chr(ord('A') + first_digit - 1)
#         count_encodings_recursive(ques[1:], ans + char_one_digit)

#     # Option 2: Encode the first two digits (if available and valid)
#     if len(ques) >= 2:
#         first_two_digits = int(ques[:2])
#         if 10 <= first_two_digits <= 26:
#             char_two_digits = chr(ord('A') + first_two_digits - 1)
#             count_encodings_recursive(ques[2:], ans + char_two_digits)

# # Example usage:
# # print("Encodings for '123':")
# # count_encodings_recursive("123")






import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())  # Runs both tasks together

asyncio.run(main())




import threading,time

# Shared variable
counter = 0

# Function to increment counter
# Lock object
lock = threading.Lock()
def increment():
    global counter
    for _ in range(10000):
        # temp = counter
        time.sleep(0.00001)
        # temp = temp +1
        #with lock:
        counter +=1

# Create threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

# Start threads
t1.start()
t2.start()

# Wait for both to complete
t1.join()
t2.join()

# Expected: 200000
print("Counter value without lock:", counter)
