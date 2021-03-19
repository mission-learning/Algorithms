#szukanie w ciagu zer i jedynek
#takiego 0 by zamienic go ns 1
#i uzyskac maksymalny ciag 1


def find_index_zero(A):
    
    max_count = 0
    index = -1
    
    prev_index = -1
    count = 0
    
    for i in range (len(A)):
        if A[i] == 1:
            count+=1
        
        else:
            count = i - prev_index
            prev_index = i
            
        if count > max_count:
            max_count = count
            index = prev_index
    
    return index
    
        