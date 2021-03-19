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
                return DFS_visit(V[index],time)
                
        time += 1
        v.process = time
        return time
        
    
    for i in range(len(G)):
        
        v = Vertex()
        v.id = i
        V.append(v)
        
    time_max = 0
    tmp = 0
        
    for v in V:
        
        if v.visited == False:
            
            tmp = DFS_visit(v,time)
            if tmp > time_max:
                time_max = tmp
    
    result = []
    
    
    for i in range(len(V)):
        
        
        result.append(time_max - V[i].entry)
    
    return result


G = [[1,5,6],[0,2,3,5],[3,1],[1,2,5,4],[3,5,6,7],[0,1,3,6],[0,5,4,7],[6,4]]
print( DFS(G) )
