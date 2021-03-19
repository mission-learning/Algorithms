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

def matrix_to_list(G):
    L = [[] for i in range (len(G))]
    
    for i in range (len(G)):
        for j in range (len(G)):
            if G[i][j] > 0:
                L[i].append([j,G[i][j]])
    
    return L

def dijkstra( G, s ,t):
    Q = []  #kolejka
    V = []  #tablica wierzcholkow
    for i in range(len(G)):
        v = Vertex()
        v.id = i
        V.append(v)
    
    V[s].d = 0
    Q.append(s)
    
    while(Q):
        u = Q.pop(0)
        for edge in G[u]:
            if relax(V,u,edge[0],edge[1]):
                Q.append(edge[0])
                
    return V[t].d



G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]

G2 = matrix_to_list(G1)

print(dijkstra(G2,5,2))

