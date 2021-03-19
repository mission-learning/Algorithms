class waggon:
    def __init__(self,number):
        self.number = number
        self.conects = []
        self.count = 0 
        
def hashfunc(number,size):
    index = ((3*number)%239)%size
    return index

def printtable(table):
    for el in table:
        if el == 0:
            print(0," ")
        else:
            print(el.number," ",el.conects)
            
            
def neighbour(wag,number):
    for el in wag.conects:
        if el != number:
            return el
        
def find_in_hash(number,hashtable,size):
    i = 0
    tmpindex = hashfunc(number,size)
    if(hashtable[tmpindex+i]):
        while(hashtable[tmpindex+i].number != number):
            i+=1
            
    return hashfunc(number,size)+i
        

def longest_train(waggons,conects):
    size = 2*len(waggons)
    hashtable = [0 for i in range (size)]
    for i in range (len(waggons)):
        tmp = waggon(waggons[i])
        if hashtable[hashfunc(waggons[i],size)] == 0:
            
            hashtable[hashfunc(waggons[i],size)] = tmp
        else:
            index = hashfunc(waggons[i],size)
            while(hashtable[index]!=0):
               index+=1
             
            hashtable [index] = tmp

    
    for con in conects:
        hashtable[hashfunc(con[0],size)].conects.append(con[1])
        hashtable[hashfunc(con[0],size)].count +=1
        
        hashtable[hashfunc(con[1],size)].conects.append(con[0])
        hashtable[hashfunc(con[1],size)].count +=1
        
    printtable(hashtable)
    
    maxsize = 0
    cursize = 0
    
    for wag in hashtable:
        if wag != 0:
            if wag.count == 0:
                cursize = 1
                index = find_in_hash(wag.number,hashtable,size)
                hashtable[index] = 0
                
            elif wag.count == 1:
                cursize+=1
                
                number = wag.number
                
                
                hashtable[find_in_hash(number,hashtable,size)] = 0
               
                index = find_in_hash(wag.conects[0],hashtable,size)
               
                wag = hashtable[index]
                hashtable[index] = 0
                
                    

                while( wag.count > 1 ):
                    
                    cursize +=1
                   
                    index = find_in_hash(neighbour(wag,number),hashtable,size)
                    
                    number = wag.number
            
                    wag = hashtable[index]
                    
                    hashtable[index] = 0
                cursize += 1
        
        if maxsize < cursize:
            maxsize = cursize
        cursize = 0
    
    return maxsize

waggons = [1,2,3,4,5,6,7,8,9,10]
conects = [(5,4),(4,1),(1,2),(7,8),(10,5),(6,7),(10,6)]

print(longest_train(waggons,conects))


