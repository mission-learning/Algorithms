#MAXHEAP

def left(i):
    return i*2

def right(i):
    return i*2+1

def size(k):
    return k[0]

def Heapify(k,i):
    l = left(i)
    r = right(i)
    maximum = i
    siz = size(k)
    if l<=siz and k[l] > k[maximum]:
        maximum = l
    if r<=siz and k[r] > k[maximum]:
        maximum = r
    if maximum != i:
        k[i],k[maximum] = k[maximum],k[i]
        Heapify(k,maximum)

def Buildheap(k):
    for i in range(int(size(k)/2),0,-1):
        Heapify(k,i)

def HeapSort(k):
    Buildheap(k)
    for i in range (size(k),1,-1):
        k[i],k[1] = k[1],k[i]
        k[0]-=1
        Heapify(k,1)
        
        
A = [0,1,2,4,6,3,5,7,45]
A[0] = len(A)-1

HeapSort(A)

print(A)
    