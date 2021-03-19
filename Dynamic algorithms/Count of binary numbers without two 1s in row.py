#dla zadanej liczby n policz wszystkie liczby w zapisie binarnym bez 2 jedynek obok siebie

def counter(n):
    
    tab = [[0 for i in range (2)] for j in range (len(n+1))]
    
    tab[1][0] = 1
    tab[1][1] = 1
    
    for i in range(2,n+1):
        tab[i][0] = tab[i-1][0] + tab[i-1][1]
        tab[i][1] = tab[i-1][0]
        
    return tab[n][0]+tab[n][1]