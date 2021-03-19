class Node:
    def __init__( self ):
        self.children = 0 # liczba dzieci wezła
        self.child = [] # lista par (dziecko, waga krawedzi)
        self.maxpath = -1000
        self.pathwith = -1000
        self.pathwithout = -1000
        self.MAX = -1000

def max_path(A):  #maksymalna sciezka od wierzcholka do liscia
    if A.children == 0:
        return 0
    
    maxpath = 0
    
    if A.maxpath != -1000:
        return A.maxpath
    
    for child in A.child:
        path =  max_path(child[0]) + child[1]
        if maxpath < path:
            maxpath = path
    
    A.maxpath = maxpath
    
    return maxpath


def heavy_path(A): #maksymalna sciezka od liscia do liscia przez wierzcholek
    if A.children == 0:
        return 0
    
    path1,path2 = 0,0
    
    for p in A.child:
        path = max_path(p[0]) + p[1]
        if path > 0:
            if min(path1,path2) < path:
                if path > path2:        #podmieniamy oba
                    path1 = path2
                    path2 = path
                else:
                    path1 = path #podmieniami mniejsza
    
    A.pathwith = path1+path2
    return A.pathwith

def path(A):
    if A.children == 0:
        return 0
    if A.pathwithout != -1000:
        return A.pathwithout
    
    pwithout = 0        #maksymalna sciezka w poddrzewie (maksymalna sciezka dziecka)
    
    pwith = 0
    
    for p in A.child:
        pwith = heavy_path(p[0]) #maksymalna sciezka przez dziecko
        if pwithout < pwith:
            pwithout = pwith
    
    A.pathwithout = pwithout
    return A.pathwithout

def ultrapath(A): #szukanie maksymalnej sciezki z 2 z wierzcholkiem i w poddrzewie
    if A.children == 0:
        return 0
    
    if A.MAX != -1000:
        return A.MAX
    
    ultra = 0   #przechowuje maksymalna sciezke mozliwa jakby rootem byl wierzcholek rozpatrywany
    
    for p in A.child:
        ultratmp = ultrapath(p[0])
        if ultra < ultratmp:
            ultra  = ultratmp
    
    A.MAX = max(ultra,heavy_path(A),path(A))
    return A.MAX
        
    
   
A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
A.children = 2
A.child = [ (B,5), (C,1) ]
B.children = 1
B.child = [(D,10)]
D.child = [[E,10],[F,20]]
D.children = 2

print(ultrapath(A))

    

