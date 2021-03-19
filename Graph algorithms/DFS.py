class Vertex():
    
    def __init__(self):
        
        self.parent = None
        self.visited = False
        self.entry = 0
        self.process = 0
        self.id = 0 
        

def DFS( G ):
    
    time = 0 
    V= []
    
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
    
    return result


G = [[1,2],[0,2,3],[3,1,0],[]]
print( DFS(G) )
