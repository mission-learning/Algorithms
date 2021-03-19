#BELLMAN FORD

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

def BF(G,s):
    V = []
    for i in range(len(G)):
        v = Vertex()
        v.id = i
        V.append(v)
        
    flag = 1
    
    
    V[s].d = 0
    
    for k in range (len(V)-1):
        for i in range (len(V)):
            for j in range (len(G[i])):
                relax(V, i, G[i][j][0], G[i][j][1])
                  
    
    for i in range (len(V)):
        for j in range (len(G[i])):
            if V[i].d + G[i][j][1] < V[G[i][j][0]].d:
                print("CYCLE")
                flag = 0
                
                
    if flag == 1:
        print(get_parent(V))
                


G = [[(1,-1)],
[(2,-2)],
[(0,0)]]
print( BF( G, 0 ) ) # wypisze [None,0,1,2]