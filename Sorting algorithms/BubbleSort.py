def sortowanie_babelkowe(lista):
    n = len(lista)
    
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
                
        n  = n - 1
        if zamien == False: break
        
    return lista
        
print(sortowanie_babelkowe([5,6,-1,0]))