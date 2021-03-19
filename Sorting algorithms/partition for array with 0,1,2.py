A = [0,1,2,0,2,1,1,2,0,1]


def swap(A,p,q):
    A[p],A[q] = A[q],A[p]

def three_partition(A):
    
    start = mid = 0
    end = len(A)-1
    p = 1   #pivot
    
    while mid <= end:
        if A[mid] < p:
            swap(A,start,mid)
            start+=1
            mid+=1
        
        elif A[mid] > p:
            swap(A,mid,end)
            end-=1
        else:
            mid+=1
    
    print(start,end)
    
    return A

print(three_partition(A))
