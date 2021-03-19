#FLOYD WARSHALL

class Vertex():
    
    def __init__(self):
        
        self.id = 0 #indeks
        self.parent = None
        self.d = 1000000 #INF
        
def relax(V,u,v,weight): #metoda relaksacji
    if V[u].d + weight < V[v].d:
        V[v].d = V[u].d + weight
        V[v].parent = u
        return True
    return False
        
def get_parent(V):  #zwraca liste parentow od listy wierzcholkow
    result = []
    for v in V:
        result.append(v.parent)
    return result

def FW(G,W):
    V = []
    for i in range(len(G)):
        v = Vertex()
        v.id = i
        V.append(v)
        
    S = [[1000 for i in range (len(V))] for i in range (len(V))]
    
    n = len(V)
    
    for i in range (n):
            for j in range (n):
                if G[i][j] > 0:
                    S[i][j] = W[i][j]
                if i == j:
                    S[i][j] = 0
    
    
    for t in range (n):
        for i in range (n):
            for j in range (n):
                S[i][j] = min(S[i][j],S[i][t] + S[t][j])
    
    return S
        
    
                

G = [[0,1,0],[1,0,1],[1,1,1]]
W = [[0,2,0],[-3,0,5],[6,3,1]]

print(FW(G,W))
