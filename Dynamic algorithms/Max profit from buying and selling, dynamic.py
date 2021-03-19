#Find maximum profit earned from at most K stock transactions

# kupujemy w jednym dniu za dana cene, sprzedajemy w dowolnym pozniejszym
# mamy maksymalnie k transakcji
#programowanie dynamiczne


price = [1,5,2,3,7,6,4,5]
K = 3

def max_profit(price,K):
    
    tab = [[0 for i in range (len(price))] for j in range (K+1)]    #tablica po dniach i liczbie k
    
    for t in range (1,K+1):
        for i in range (len(price)):
            
            max_prof = 0
            
            for j in range (0,i):   # zliczamy maksymalny profit do dnia i
                
                profit = price[i] - price[j] + tab[t-1][j]  # dla kazdego j od 0 do i-1, profit to roznica cen w i oraz j dodac profit maksymalny do dnia jotego 
                max_prof = max(max_prof,profit)
            
            tab[t][i] = max(tab[t][i-1],max_prof) #maksymalny profit do dnia i przy t okresach to albo maksymalny do dnia wczesniej albo maksymalny uzyskany przy zakonczeniu transakcji w dniu i
    
    return tab[K][len(price)-1]
            
    
    
print(max_profit(price, K))
    
    
    
    
    
    
    
    
    
    
    
    
    
    