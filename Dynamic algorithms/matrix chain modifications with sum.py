def absolute(a):
    if a < 0:
        return -a
    return a


def sum_absolute(A):
    tab = [[1000 for i in range (len(A))] for i in range (len(A))]
    maxval = [[1000 for i in range (len(A))] for i in range (len(A))]
    
    size = len(A)
    
    for i in range (size):
        tab[i][i] = A[i]
        maxval[i][i] = 0
    
    for l in range (1,size):
        for i in range (0,size-l):
            
            j = i + l
            
            for m in range (i,j):
                
                abl = tab[i][m]+tab[m+1][j]
                abla = max(absolute(abl),maxval[i][m],maxval[m+1][j])
                
                if maxval[i][j] > abla:
                    
                    tab[i][j] = abl
                    maxval[i][j] = abla
                    
    
    return maxval[0][size-1]

                

A = [3, 6, 9, -8, -6, -3]
print(sum_absolute(A))
