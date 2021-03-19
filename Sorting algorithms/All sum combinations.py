def printCombinations(A, i, sum, sum_left):

    prev_num = A[i - 1] if (i > 0) else 1
    
    for k in range(prev_num, sum + 1):
        
        A[i] = k
        
        if sum_left > k:
            printCombinations(A, i + 1, sum, sum_left - k)

		# if sum is found
        if sum_left == k:
            print(A[:i+1])

def findCombinations(sum):

	A = [0 for i in range (sum)] 

	starting_index = 0
	printCombinations(A, starting_index, sum, sum)




sum = 5
findCombinations(sum)