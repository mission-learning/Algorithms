#uniwersalne ujscie

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

def turn_back(G):
    Gprim = [[0 for i in range (len(G))] for i in range (len(G))]
    for i in range (len(G)):
        for j in range (len(G)):
            if G[i][j] == 1:
                Gprim[j][i] = 1
    return Gprim


def find_t(G):
    result = []
    for i in range (len(G)):
        flag = 0
        for j in range (len(G)):
            if G[i][j] == 1:
                flag = 1
                break
        if flag == 0:
            result.append(i)
    
    return result
            


def Universal_ujscie(G):
    
    pot_t = find_t(G)
    
    G = turn_back(G)
    
    flag = 1
    
    Q = []
    V = []
    for i in range(len(G[0])):
        v = Vertex()
        v.id = i
        V.append(v)
        
    for s in pot_t:
        for v in V:
            v.visited = False
        
        V[s].visited = True
        Q.append(V[s])
        
        while len(Q) > 0:
            
            u = Q.pop(0)
            neighbours = index(G,u.id)
            for i in range(len(neighbours)):
                
                if V[neighbours[i]].visited == False:
                
                    V[neighbours[i]].visited = True
                    
                    Q.append(V[neighbours[i]])
                    
        for el in V:
            if el.visited == False:
                flag = 0
        
        if flag == 1 :
            return V[s].id
        
    return None
       
    
G = [[0,1,1,0],[0,0,0,1],[0,0,0,0], [0,0,0,0]]
print (Universal_ujscie(G)) 
