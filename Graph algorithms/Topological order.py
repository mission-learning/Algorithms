class Vertex():
    
    def __init__(self):
        
        self.parent = None
        self.visited = False
        self.entry = 0
        self.process = 0
        self.id = 0 
        
stack = []

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
                
        stack.insert(0,v.id)
                
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


G = [[1,5,6],[0,2,3,5],[3,1],[1,2,5,4],[3,5,6,7],[0,1,3,6],[0,5,4,7],[6,4]]
print( DFS(G) )
print(stack) #topologiczne
 