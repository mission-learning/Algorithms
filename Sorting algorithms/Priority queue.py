#kolejka priorytetowa

def parrent(i):
    return i/2

def getmax(k):
    if size(k) == 0: 
        sys.exit()
    result = k[1]
    k[1] = k[size(k)]
    k[0]-=1
    heapify(k,1)
    return result

def insert(k,x):
    if k[0] < len(k)-1:
        k.append(x)
        k[0]+=1
    k[size(k)]=x
    i = size(k)
    while(i>1 and k[i]>k[parrent(i)]):
        k[i],k[parrent(i)] = k[parrent(i)],k[i]
    
    S