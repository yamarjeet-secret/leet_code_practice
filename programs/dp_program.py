def dicecombinations():
    maxN = int(1e6)
    MOD = int(1e9+7)
    N = int(input())
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        for j in range(1, 7):
            if i-j >= 0:
                dp[i] = (dp[i] + dp[i-j]) % MOD
            else:
                break
    print(dp[N])


def min_coins():
    inp = input()
    inp = list(map(int,inp.split()))
    arr = input()
    arr = list(map(int,arr.split()))
    N = inp[0]
    target_sum = inp[1]
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0

    for coin in arr:
        for i in range(coin, target_sum + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target_sum] if dp[target_sum] != float('inf') else -1


from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == '__main__':
    with Pool(4) as p:  # Pool size of 4 processes
        numbers = [1, 2, 3, 4, 5]
        squares = p.map(square, numbers)
        print(squares)
