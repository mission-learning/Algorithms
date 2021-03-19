#min coins

coins = [1, 3, 5, 7]
N = 18


def minCoins(S, N):

    T = [0 for i in range (N + 1)]

    for i in range(1, N + 1):

        T[i] = 10000

        for coin in range(len(coins)):
          
            if i - S[coin] >= 0:
                result = T[i - S[coin]]
                
                if result != 10000:
                    T[i] = min(T[i], result + 1)

    return T[N]



count = minCoins(coins, N)
if count != 10000:
    print("Minimum number of coins required to get desired change is", count)