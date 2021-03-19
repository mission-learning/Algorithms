#KRUSKALA
#posortuj krawedzie rosnaco
#stworz zbior pusty A
#przegladaj krawedzie w kolejnosci rosnacych wag
#ElogV


from find import *

class e:
    def __init__(self,start,end,w):
        self.start = start
        self.end = end
        self.w = w

def sort(G): #dodawanie i sortowanie krawedzi do zbioru G
    result = []
    for i in range (len(G)):
        for j in range (len(G[i])):
            edge = e(i,G[i][j][0],G[i][j][1])
            result.append(edge)
            
    result = sorted(result,key = lambda e : e.w)
    return result
    
    
def Kruskal(G):
    #sortowanie rosnaco krawezi po wagach
    edges = sort(G)
    
    A = []
    
    V = make_set(G)
    
    for edge in edges:
        if find_set(V[edge.start]) != find_set(V[edge.end]): #jezeli nowa krawedz nie zawiera cyklu
	#czyli poczatek i koniec musza nalezec do roznych zbiorow set
            A.append(edge)
            union(V[edge.start],V[edge.end]) #wrzucamy do jednego zbioru poczatek i koniec krawedzi
    
    for el in A:
        print(el.start,el.end)
  


G = [[[1,5],[4,2]],[[2,7]],[[0,100],[4,80],[3,20]],[[4,3]],[]]

Kruskal(G)
