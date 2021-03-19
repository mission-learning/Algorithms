def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r], A[i+1]
    return i+1



def Quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A, q+1,r)


A = [3,4,6,8,3,0]
Quicksort(A,0,len(A)-1)
print(A)
