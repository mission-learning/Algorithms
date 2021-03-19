class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
        self.index = -1
       
N = 20

def h(key,N):
    
    v = (key*13)%27
    
    
    return v % N


def insert(hash_tab, key,j):
    idx = h(key,len(hash_tab))
    for i in range(len(hash_tab)):
        if hash_tab[idx].taken:
            idx = (idx + 1) % N
        else:
            break
    
    if not hash_tab[idx].taken:
        hash_tab[idx].key = key
        hash_tab[idx].taken = True
        hash_tab[idx].index = j


def find(hash_tab, key):
    idx = h(key,len(hash_tab))
    for i in range(len(hash_tab)):
        if not hash_tab[idx].taken: return None,None
        if hash_tab[idx].key == key: return idx,hash_tab[idx].index
        idx = (idx + 1) % (len(hash_tab))
    
    return None,None


def find_subarray_sum_0(A):
    hash_t = []
    
    for i in range (2*(len(A))):
        a = Node()
        hash_t.append(a)
    
    sum = 0
    
    for i in range(len(A)):
        
        sum += A[i]
        index,id = find(hash_t,sum)
        
        if index != None:
            print("Subarray:",id+1,":",i)
        insert(hash_t,sum,i)
        
    
A = [3,4,8,3,1,3,1,-4,2,2]    
find_subarray_sum_0(A)