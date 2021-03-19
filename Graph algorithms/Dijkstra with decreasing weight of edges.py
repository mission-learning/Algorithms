class Vertex():
    
    def __init__(self):
        
        self.id = 0 #indeks
        self.parent = None
        self.d = 1000000 #INF
        self.w = -1
        
def relax(V,u,v,weight): #metoda relaksacji
    if V[u].d + weight < V[v].d and V[u].w > weight:
        V[v].d = V[u].d + weight
        V[v].parent = u
        V[v].w = weight
        return True
    return False

def dijkstra( G, s ,en):
    Q = []  #kolejka
    V = []  #tablica wierzcholkow
    for i in range(len(G)):
        v = Vertex()
        v.id = i
        V.append(v)
    
    
    for e in G[s]:
        V[e[0]].d = e[1]
        V[e[0]].w = e[1]
        V[e[0]].parent = s
        Q.append(e[0])
    
    while(Q):
        u = Q.pop(0)
        for edge in G[u]:
            if relax(V,u,edge[0],edge[1]):
                Q.append(edge[0])
                
    if V[en].parent == None:
        return 100000
    else:
        return V[en].d


G = [[(3,2), (2,15)],
[(2,10), (3,18)],
[(1,10),(0,15)],
[(0,2),(1,18)]]
print( dijkstra( G, 0,1 ) ) 
        