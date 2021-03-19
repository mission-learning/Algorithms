def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x,n,deph): 
    arr = [] 
    for i in range(10): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in x: 
        index_b = int((j*deph)%10)  
        arr[index_b].append(j) 
        
    for element in arr:
        if len(element)>n:
            element = bucketSort(element,n,deph*10)
      
    # Sort individual buckets  
    #for i in range(slot_num): 
      # arr[i] = insertionSort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(10): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x 

x = [5.3,5.2,7.5,9,6,4,2,3,5.8]
print(bucketSort(x,5,1))