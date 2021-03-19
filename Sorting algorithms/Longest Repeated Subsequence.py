def LRSlength(x,i,j):
    if i == 0 or j == 0:
        return 0
    if x[i-1] == x[j-1] and i != j:
        return LRSlength(x,i-1,j-1) + 1
    return max(LRSlength(x,i-1,j),LRSlength(x,i,j-1))


x = 'dodmoimitto' 
print(LRSlength(x,len(x),len(x)))
       