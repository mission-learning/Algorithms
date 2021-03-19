class Vertex():
    
    def __init__(self):
        
        self.visited = False
        self.parent = None
        self.d = 0
        self.id = 0
        

def index(G, u):
    
    borders = []
    for i in range(len(G[0])):
        
        if G[u][i] == 1:
            
            borders.append(i)
            
    return borders



def BFS( G, s ):
    
    Q = []
    V = []
    for i in range(len(G[0])):
        v = Vertex()
        v.id = i
        V.append(v)
    
    V[s].visited = True
    Q.append(V[s])
    
    while len(Q) > 0:
        
        u = Q.pop(0)
        neighbours = index(G,u.id)
        for i in range(len(neighbours)):
            
            if V[neighbours[i]].visited == False:
            
                V[neighbours[i]].visited = True
                V[neighbours[i]].d = u.d + 1
                V[neighbours[i]].parent = u.id
                
                Q.append(V[neighbours[i]])
    result = []
    for i in range(len(V)):
        result.append((V[i].parent,V[i].d))
    return result


          
    
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print (BFS(G,0)) 




        
