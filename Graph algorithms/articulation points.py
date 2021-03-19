#punkty artykulacji graf nieskierowany

#uruchamiamy dfs i obliczamy funkcje low

#jezeli korzen posiada wiecej niz 1 syna jest punktem artykulacji

#jesli v posiada syna takiego ze low(syn) >= d(v)
#to v jest punktem artykulacji

class Vertex():
    
    def __init__(self):
        
        self.parent = None
        self.visited = False
        self.entry = 0
        self.id = 0 
        self.low = 1000
        self.children = []
        

def indexes (G, u): #zwraca dzieci
    
    borders = []
    for i in range(len(G[0])):
        
        if G[u][i] == 1:
            
            borders.append(i)
            
    return borders

def lowchild(V,N): #zwraca najmniejsze low wsrod dzieci
    low = 1000
    for n in N:
        if low > V[n].low:
            low = V[n].low
    return low
        
def lowgreatestchild(V,N):
    low = -1
    for el in N:
        if low <= V[el].low:
            low = V[el].low
    return low
    

def DFS( G,V ):
    
    time = 0 
    
    def DFS_visit(V,v,time):
                
        time += 1
        v.visited = True
        v.entry = time
        
        N = indexes(G,v.id)
        v.low = v.entry
        #poczatek, tu jeszcze nie mamy dzieci i krawedzi wstecznych wiec wpisujemy czas odwiedzenia
        
        for index in N:
            
            if V[index].visited == False:
                v.children.append(index) #dodajemy dzieci w drzewie DFS
                V[index].parent = v.id
                DFS_visit(V,V[index],time)
                
            elif v.parent != index: #jesli trafilismy na odwiedzony wierzcholek czyli mamy krawedz wsteczna
                v.low = min(v.low,V[index].entry)
                
        time += 1
        
        #uaktualniamy low po przetworzeniu
        
        if len(v.children)>0:
            v.low = min(v.low,v.entry,lowchild(V,v.children))
        else:
            v.low = min(v.low,v.entry)
        

    DFS_visit(V,V[0],time)
    
    result = []
    
    if len(V[0].children)>1:
        result.append(0)
    
    for i in range (1,len(V)):
        if lowgreatestchild(V,V[i].children)>= V[i].entry:
            result.append(i)
   
    
    return result

G = [[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
V = []

for i in range(len(G)): 
      v = Vertex()
      v.id = i
      V.append(v)
        

print(DFS(G,V))


