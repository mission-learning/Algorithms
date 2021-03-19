def countingSort(A,j):

    
    k = 10 
    n=len(A)
    B=[0]*n
    C=[0]*k


    for i in range(k): C[i] = 0

    for i in range(n): C[get_digit(A[i],j)] += 1

    for i in range(1,k): C[i] += C[i-1]

    for i in range(n-1, -1, -1):

        C[get_digit(A[i],j)] -= 1

        B[C[get_digit(A[i],j)]] = A[i]

    for i in range(n): A[i] = B[i]


def get_digit(number, n):
    return number // 10**n % 10

def ile(A):

    dlugosc = len(str(A[0]))

    return dlugosc

def sortusortu(A):

    for i in range(ile(A)):

        countingSort(A,i)




asd=[1003,1865,3275,1230,7342, 8456, 3210, 6784, 3745, 8601]

sortusortu(asd)

print(asd)











        
