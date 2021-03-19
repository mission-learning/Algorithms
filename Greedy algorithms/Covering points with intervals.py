def find_intervals_1(A):
    end = -1
    count = 0
    start = -1
    result = []
    
    for j in range (len(A)):
        if A[j] > end:
            start = A[j]
            end = A[j] + 1
            count += 1
            result.append([start,end])
            
    return result
       

A = [0.25,0.5,1.6]
A = sorted(A)
print(A)

print(find_intervals_1(A))