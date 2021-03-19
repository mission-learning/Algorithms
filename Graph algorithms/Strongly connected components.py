#silnie spojne skladowe

class Vertex():
    
    def __init__(self):
        
        self.parent = None
        self.visited = False
        self.entry = 0
        self.process = 0
        self.id = 0 
        

def DFS( G,V ):
    
    time = 0 
    
    def DFS_visit(v,time):
                
        time += 1
        v.visited = True
        v.entry = time
        
        for index in G[v.id]:
            
            if V[index].visited == False:
                
                V[index].parent = v.id
                DFS_visit(V[index],time)
                
        time += 1
        v.process = time
        
    
    for i in range(len(G)):
        
        v = Vertex()
        v.id = i
        V.append(v)
        
    for v in V:
        
        if v.visited == False:
            
            DFS_visit(v,time)
    
    result = []
    
    for i in range(len(V)):
        
        result.append(V[i].parent)
    
    return V

def DFS_finder(V,G,v,result):
    
    v.visited = True
    result.append(v.id)
        
    for index in G[v.id]:
            
        if V[index].visited == False:
                
            V[index].parent = v.id
            result = DFS_finder(V,G,V[index],result)
            
    return result
    

def turn_back_edges(G):
    Gprim = [[]for i in range (len(G))]
    
    for i in range (len(G)):
        for e in G[i]:
            Gprim[e].append(i)
            
    return Gprim
    

def spojne_skladowe(G):
    #dfs z zapisaniem czasu przetworzenia
    V = []
    V = DFS(G,V)
 
        
    #odwrocenie krawedzi
    #DFS jeszcze raz w kolejnosci malejacych czasow przetworzenia
    
    #odnalezione paczki to spojne skladowe
     
    Gprim = turn_back_edges(G)
    print(Gprim)
    
    V = sorted(V,key = lambda vertex:vertex.process,reverse = True)
    
    for el in V:
        el.visited = False
    
    for el in V:
        res = []
        res = DFS_finder(V,Gprim,el,[])
        print(res)
    


G = [[1,2],[0,2,3],[3,1,0],[]]
spojne_skladowe(G)


