#TERMINY GONIO

class task:
    def __init__(self,d,g):
        self.g = g
        self.d = d

         
            
        
def partition(A,p,r):
    x = A[r].d
    i = p-1
    for j in range(p,r):
        if A[j].d <= x:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r], A[i+1]
    return i+1

def Quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A, q+1,r)
        

def taskreal(T):
    count = 0
    time = 0
    
    result = []
    
    for el in T:
        time = el.d
        
        if time > count:
            result.append(el.g)
            count+=1
        else:
            minimum = min(result)
            if el.g > minimum:
                result.remove(minimum)
                result.append(el.g)
    print(result)
    
        
T = []
T.append(task(1,1))
T.append(task(2,2))
T.append(task(3,3))
T.append(task(3,100))
T.append(task(3,100))

Quicksort(T,0,len(T)-1)

taskreal(T)

























        
        