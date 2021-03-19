#PRIM

#zaczynamy od korzenia drzewa
#przetwarzamy wierzcholki wyciagajac je z kolejki jak bfs
#relaksujemy po sasiadach

class Vertex():
    
    def __init__(self):
        
        self.id = 0 #indeks
        self.parent = None
        self.d = 1000000 #INF
        
        
def relax_prim(V,u,v,weight): #metoda relaksacji
    if weight < V[v].d:
        V[v].d = weight
        V[v].parent = u
        return True
    return False
        
def get_parent(V):  #zwraca liste parentow od listy wierzcholkow
    result = []
    for v in V:
        result.append(v.parent)
    return result


def PRIM( G, s ):
    Q = []  #kolejka #tu powinna byc kolejka priorytetowa, ale uaktualniajac zawsze po relaksacji dalej ok
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
            if relax_prim(V,u,edge[0],edge[1]):
                Q.append(edge[0])
                
    return get_parent(V)


G = [[(1,0), (2,1)],
[(3,1), (2,0)],
[(3,0)],
[]]
print( PRIM( G, 0 ) ) # wypisze [None,0,1,2]
        