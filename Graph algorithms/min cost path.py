class Vertex():
    
    def __init__(self):
        
        self.cost = 10000 #koszt pierwotny, zakladam,ze drog jest mniej niz 10 000
        self.id = 0 #indeks
        self.depth = 0 #maksymalna glebokosc szukania
        

def path_cost( G, s ,t):
    
    Q = []
    V = []
    for i in range(len(G)):
        v = Vertex()
        v.id = i
        V.append(v)
    
    # tworzenie wierzcholkow w liscie V
        
    V[s].cost = 0 #dojscie ze startu do startu kosztuje 0
    
    Q.append(V[s])
    
    while len(Q) > 0:
        
        u = Q.pop(0)
        
        for i in range(len(G[u.id])):
            
                #wyznaczenie minimalnego kosztu dojscia do wierzcholka o danym indeksie
                # koszt = min(starty koszt, koszt parenta + koszt sciezki)
                
                V[G[u.id][i][0]].cost = min( V[G[u.id][i][0]].cost,
                                            V[u.id].cost + G[u.id][i][1]) 

                
                V[G[u.id][i][0]].depth +=1 
                
            
                if (V[G[u.id][i][0]].depth < len(G)) or G[u.id][i][0] == t:
                    
                    Q.append(V[G[u.id][i][0]])
                    
    return V[t].cost



G = [[(1,1), (2,1)],
[(3,1), (2,1)],
[(3,0)],
[]]
print( path_cost( G, 0, 3 ) ) # wypisze 0



        
