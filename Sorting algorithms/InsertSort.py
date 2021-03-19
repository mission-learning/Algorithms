def Insert_sort(A):
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j>=0 and A[j]>klucz:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
        
        