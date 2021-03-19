#number of ways of coin change


coins = [1,2,3,5,7]

amount = 6

def coin_change(coins,amount):
    
    tab = [[ 0 for i in range (amount+1)] for j in range (len(coins)+1)]
    
    for i in range (len(coins)+1):
        tab[i][0] = 1
    
    
    for i in range (1,(amount+1)):
            if i % coins[0] == 0:
                tab[1][i] = 1

    for i in range (1,len(coins)+1):
        for j in range (1,(amount+1)):
            if coins[i-1] <= j:
                tab[i][j] = tab[i-1][j] + tab[i][j-coins[i-1]]
            else:
                tab[i][j] = tab[i-1][j]
    
    print(tab[len(coins)][amount])
    
coin_change(coins, amount)
            