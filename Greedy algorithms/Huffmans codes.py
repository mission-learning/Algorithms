def huffman_len(A,B,C):
    if len(B) == 1:
        result = 0
        for i in range (len(A)):
            result += A[i]*C[i]
        return result
    print(B)
    
    indexes = []
    
    lowest = B[0][0]
    lowest_id = 0
    
    for i in range (len(B)):
        if lowest > B[i][0]:
            lowest = B[i][0]
            lowest_id = i
    indexes += B[lowest_id][1]
    del B[lowest_id]
    
    sec_low = B[0][0]
    sec_low_id = 0
    for i in range (len(B)):
        if sec_low > B[i][0]:
            sec_low = B[i][0]
            sec_low_id = i
    indexes += B[sec_low_id][1]
    del B[sec_low_id]
    
    B.append([sec_low+lowest,indexes])
    for i in range (len(B[len(B)-1][1])):
        C[B[len(B)-1][1][i]]+=1
        
        
    return huffman_len(A,B,C)
    
 
    
A = [ 200, 700, 180, 120, 70, 30]
C = [0 for i in range (len(A))]   
B = []   
for i in range(len(A)):
    B.append([])
    B[i].append(A[i])
    B[i].append([i])
print(huffman_len(A,B,C))
print(C)