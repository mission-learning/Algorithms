def matrixChainMultiplication(dims):

	n = len(dims)

	c = [[0 for i in range(n + 1)] for j in range((n + 1))]

	for length in range(2, n + 1):  

		for i in range(1, n - length + 2):

			j = i + length - 1
			c[i][j] = 100000

			k = i
            
			while j < n and k <= j - 1:
				cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]

				if cost < c[i][j]:
					c[i][j] = cost

				k = k + 1

	return c[1][n - 1]

dims = [1,2,5]

print(matrixChainMultiplication(dims))
