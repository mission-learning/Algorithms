#majac k posortowanych list
#scal w jedna posortowana liste

class Node:
    def __init__(self,index,i,value):
        self.val = value
        self.index = index
        self. i = i
        
        
#MINHEAP

def left(i):
    return i*2

def right(i):
    return i*2+1

def size(k):
    return k[0]

def Heapify(k,i):
    l = left(i)
    r = right(i)
    minimum = i
    siz = size(k)
    
    if l<=siz and k[l].val < k[minimum].val:
        minimum = l
    if r<=siz and k[r].val < k[minimum].val:
        minimum = r
    if minimum != i:
        k[i],k[minimum] = k[minimum],k[i]
        Heapify(k,minimum)
        
def Buildheap(k):
    for i in range(int(size(k)/2),0,-1):
        Heapify(k,i)

A = [[1,3,6,7],[2,4,8,23],[5,9,12,14],[11,13,25]]
k = 4

def merge_k_lists(A,k):
    
    heap = [len(A)]
    
    for i in range (len(A)):
        a = Node(i,0,A[i][0])
        heap.append(a)

    result = []
    
    Buildheap(heap)
    x = 0
    
    while size(heap) > 0:
       
        result.append(heap[1].val)
        #dodajemy minimum
        
        
        if heap[1].i + 1 < len(A[heap[1].index]):
            #jesli nastepny element z tej samej listy co minimum istnieje
               
            heap[1] = Node(heap[1].index,heap[1].i+1,A[heap[1].index][heap[1].i+1])
            #dodajemy go do listy na miejsce minimum

        else:
            heap[1] = heap[heap[0]]
            heap[0]-=1
            #w przeciwnym razie zmniejszamy rozmiar heapa i przepisujemy ostatni element do pierwszego
            
        Heapify(heap,1)
        
    print(result)
            
    
    
merge_k_lists(A,k)
        


        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
