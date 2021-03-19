
class Vertex:
    def __init__(self,index):
        self.id = index
        self.neighbours = []

def graph(A):
    V = []
    for i in range(len(A)):
        v = Vertex(i)
        v.neighbours = A[i]
        V.append(v)
    
    return V
        
def DFS(V,stack,result):
    
    v = stack[len(stack)-1] #stos
    
    for n in v.neighbours: 
        #przechodzimy po sasiadach
        
        stack.append(V[n])            
        v.neighbours.remove(n)  #usuwamy krawedz
        V[n].neighbours.remove(v.id)
        DFS(V,stack,result) #uruchamiamy dalej

    result.append( stack.pop().id ) #dodajemy wierzcholek po przetworzeniu
    return result


A = [[1,2],[0,2],[0,1,3,4],[2,4],[2,3]]
V = graph(A)

stack = []
result = []
stack.append(V[0])
print(DFS(V,stack,result))