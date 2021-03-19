class Vertex():
    
    def __init__(self):
        
        self.visited = False
        self.id = 0
        self.num = -1
        

def index(G, u):
    
    borders = []
    for i in range(len(G[0])):
        
        if G[u][i] == 1:
            
            borders.append(i)
            
    return borders



def BFS( G, s):
    
    Q = []
    V = []
    for i in range(len(G[0])):
        v = Vertex()
        v.id = i
        V.append(v)
    
    V[s].visited = True
    V[s].num = 0
    
    Q.append(V[s])
    
    while len(Q) > 0:
        
        u = Q.pop(0)
        num = u.num
        
        neighbours = index(G,u.id)
        for i in range(len(neighbours)):
            
            if V[neighbours[i]].visited == False:
            
                V[neighbours[i]].visited = True
                if  V[neighbours[i]].num == num:
                    return False
                elif V[neighbours[i]].num == -1:
                    if num == 0:
                        V[neighbours[i]].num = 1
                    else:
                        V[neighbours[i]].num = 0

                Q.append(V[neighbours[i]])
                
            else:
                if  V[neighbours[i]].num == num:
                    return False
                
    for el in V:
        print(el.num)
                
    return True
 
    
G = [[0,0,0,1],[0,0,1,0],[0,1,0,1],[1,0,1,0]]
print (BFS(G,0)) 

