class Vertex():
    
    def __init__(self):
        
        self.parent = None
        self.visited = False
        self.id = 0 
        self.black = False
        
def DFS( G,x,y,V ):

    def DFS_visit(V,v,p1,p2):
        
        v.visited = True
        
        neighbours = G[v.id]
        
        for index in neighbours:

            p1tmp = index[1] - 5
            p2tmp = index[1] + 5
            
            if V[index[0]].visited == False and ((p1 == 0 and p2 == 0) or p1 < index[1] < p2):
              
                V[index[0]].parent = v.id
                
                if p1 != 0 and p2 != 0:
                
                    if p1tmp > p1:
                        if p2tmp < p2:
                            DFS_visit(V,V[index[0]],p1tmp,p2tmp)
                        else:
                            DFS_visit(V,V[index[0]],p1tmp,p2)
                    elif p2tmp < p2:
                         DFS_visit(V,V[index[0]],p1,p2tmp)
                    else:
                         DFS_visit(V,V[index[0]],p1,p2)
                        
                      
                else:
                    DFS_visit(V,V[index[0]],p1tmp,p2tmp)
                    
        v.visited = False
        
    DFS_visit(V,V[0],0,0)
    
    if V[y].parent != None:
        return True
    else:
        return False
    


G = [[[1,10],[2,20]],[[0,10],[2,7],[3,15]],[[0,20],[1,7],[3,11]],[[1,15],[2,11]]]
V = []
for i in range(len(G)):
       v = Vertex()
       v.id = i
       V.append(v)
       
print (DFS(G,0,3,V)) 




        
