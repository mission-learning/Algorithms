A = [1,4,7,3,8]

def sumsub(A,s):
    B = [[0 for i in range (s+1)] for i in range(len(A)+1)]
    
    for i in range(len(A)+1):
        B[i][0] = 1
        
    
    for i in range(1,len(A)+1):
        for j in range (1,s+1):
            if j - A[i-1] >= 0:
                B[i][j] = B[i-1][j] or B[i-1][j-A[i-1]]
            else:
                B[i][j] = B[i-1][j]

                
    print(B[len(A)][s])
    
      
sumsub(A,8)