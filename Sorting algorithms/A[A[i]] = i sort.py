#zmientablice tak, by A[A[i]]= 0 stala pamiec, liniowo

A = [1,3,4,2,0]


def change(A):
    
    to_put = 0
    to_go = A[0]
    k = -1
    i = 0
    while k < len(A) :
        k+=1
        
        to_go_next = A[to_go]
        A[to_go] = to_put
        
        to_put = to_go
        to_go = to_go_next
        
    print(A)
    
change(A)
        
        
        