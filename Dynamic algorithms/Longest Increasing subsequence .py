#longest increasing subsequence z najdłuższym wspólnym podciagiem

def longestcomsub(A,B,x):
    
    if(len(A)>0 and len(B)>0):
        if A[len(A)-1] == B[len(B)-1]:
            x += 1
            return longestcomsub(A[:-1],B[:-1],x)
        else:
            return max(longestcomsub(A[:-1],B,x),longestcomsub(A,B[:-1],x))
    
    return x


A = [2,4,7,2,4,0,1,3]
B = sorted(A)


print(longestcomsub(A,B,0))
