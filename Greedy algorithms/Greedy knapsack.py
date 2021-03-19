def maxprofit(B,k,profit):
    if k == 0: 
        return profit
    result = 0
    result_id = 0
    for i in range (len(B)):
        if result < B[i][0]:
            result = B[i][0]
            result_id = i
   
    if B[result_id][1] < k:
        profit += B[result_id][0]*B[result_id][1]
        k -=B[result_id][1]
    else:
        profit += B[result_id][0]*k
        k = 0
    del B[result_id]
    return maxprofit(B, k, profit)
    


def knapsack(A, k):
    B = []
    for i in range (len(A)):
        B.append([])
        B[i].append(A[i][0]/A[i][1])
        B[i].append(A[i][1])
    return maxprofit(B,k,0)
    

print(knapsack([ (1,1), (10,2), (6,3) ], 3))