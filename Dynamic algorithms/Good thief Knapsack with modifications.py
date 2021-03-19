#goodTHIEF
#knapsack problem z ograniczeniem w formie takiej, ze nie wolno brac rzeczy obok siebie


def knapSack(W, weights, values, size): 
    K = [[0 for i in range(W + 1)] for j in range(size + 1)] 
  
    for i in range(size + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif weights[i-1] <= w: 
               if i >=2:
                   K[i][w] = max(values[i-1] + K[i-2][w-weights[i-1]], K[i-2][w], K[i-1][W]) 
		#bierzemy stan sprzed poprzedniego elementu biorac element/nie biorac/bierzemy stan poprzedniego elementu
               else:
                   K[i][w] = max(values[i-1], K[i-1][w]) 
                       
            
            else: 
                K[i][w] = K[i-1][w] 
  
    return items_got(K,size,W,values,weights)
  


def items_got(K,size,W,values,weights):
    i = size
    j = W
    result = []
    sume = 0
    
    while i >= 2:
        if K[i][j] == K[i-2][j - weights [i-1] ] + values[i-1] :
            sume += values[i-1]
            
            result.insert(0,i-1)
            i-=2
            j -= weights [i-1] 
        else:
            i-=1
            
    if i == 1:
        if values[i-1] + sume == K[size][W]:
            result.insert(0,i-1)
        
        
    return result
    


values = [10,200,100,20,500] 
weights = [10,10,10,10,10] 
w = 50
size = len(values) 
print(knapSack(w, weights, values, size)) 