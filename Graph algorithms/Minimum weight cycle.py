#dla kazdego wierzcholka uruchamiamy dijkstre z modyfikacja
#relaksacji przez dodanie atybutu mincycle
#zapisujemy w nim minimalny cykl z danym wierzcholkiem
#zwracamy wielkosc cyklu oraz kolejne wierzcholki wchodzace w cykl

class Vertex():
    
    def __init__(self):
        
        self.id = 0 #indeks
        self.parent = None
        self.d = 1000000 #INF
        self.mincycle = 1000
        
def relax(V,u,v,weight,s): #metoda relaksacji
    if v == s and V[u].d + weight < V[v].mincycle:
        V[v].d = V[u].d + weight
        V[v].parent = u
        V[v].mincycle = V[u].d + weight
        return False  

    if V[u].d + weight < V[v].d:
        V[v].d = V[u].d + weight
        V[v].parent = u
        return True
    return False

def cycle(V,s):
    result = [s]
    v = s
    while V[s].parent != v:
        s = V[s].parent
        result.insert(0,s)
        
    return result


def dijkstra( G, s ):
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
            if relax(V,u,edge[0],edge[1],s):
                Q.append(edge[0])
                
    if V[s].parent == None:
        return 10000,[]      
    
    return V[s].mincycle,cycle(V,s)

def mincycle(G):
    res = []
    mincycle = 10000
    for v in range (len(G)):
        tmp,cycle = dijkstra(G,v)
        if mincycle > tmp:
            res = cycle
    return res

G = [[(4,50)],
[(0,10)],
[(0,100),(1,2)],
[(2,3)],
[(2,200),(3,5)]]

print( mincycle( G ) ) # wypisze [None,0,1,2]
        