def matrix_to_list(G):
    L = [[] for i in range (len(G))]
    
    for i in range (len(G)):
        for j in range (len(G)):
            if G[i][j] > 0:
                L[i].append([j,G[i][j]])
    
    print (L)
    return L

def list_to_matrix(L):
    
    G = [[0 for i in range (len(L))] for i in range (len(L))]
    
    
    for i in range (len(L)):
        for j in range (len(L[i])):
            G[i][L[i][j][0]] = L[i][j][1]
    
    print(G)
    return G
    







G = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 

