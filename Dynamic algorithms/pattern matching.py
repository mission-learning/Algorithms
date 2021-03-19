#pattern matching with dynamic programming

pattern = "x?y*z"

tocheck = "xdydbfdfekz"

def check(pattern,to_check):
    
    size_p = len(pattern)+1
    size_t = len(to_check)+1
    
    T = [[False for i in range (size_p)] for j in range (size_t)]
    
    T[0][0] = True
    
    flag = 1
    
    for i in range (1,size_p):
        if pattern[i-1] == "*" and flag == 1:
            
            T[i][0] = True
            
        else:
            flag = 0
    
    for i in range (1,size_t):
        for j in range (1,size_p):
            
            if pattern[j-1] == to_check[i-1] or pattern[j-1] == "?":
                T[i][j] = T[i-1][j-1]
            elif pattern[j-1] == "*":
                T[i][j] = (T[i-1][j] or T[i][j-1])
            else:
                T[i][j] = False
             
    return T[size_t-1][size_p-1]
    
    
print(check(pattern,tocheck))