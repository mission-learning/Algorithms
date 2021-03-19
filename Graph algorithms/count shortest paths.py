class Vertex():
    
    def __init__(self):
        
        self.id = 0 
        self.visited = False
  
def minimal(lista): #zwraca z listy mozliwych sciezek liczbe najkrotszych sciezek

    minim = min(lista)

    counter = 0
    for element in lista:
        if element == minim:
            counter += 1
            
    return counter

def index(G, u): #zwraca liste sasiadow dla danego wierzcholka
    
    borders = []
    for i in range(len(G[0])):
        
        if G[u][i] == True: # jezeli jest sasiadem dodaj do listy borders
            
            borders.append(i)
            
    return borders

def count_paths( G, u, t, V, path_count, path):  #zlicza dlugosci sciezek i wpisuje do listy
    
        V[u].visited = True #umozliwia niezapetlenie sie danej sciezki
        if (u == t): 
            #jezeli dotarlismy do koncowego wierzcholka dodajemy dlugosc trasy do listy
            path_count.append(path)
            print(path_count) #tak wyglada lista mozliwych dlugosci sciezek
        else: 
            neighbours = index(G,u)
            for v in neighbours:
                if (V[v].visited == False):  #jezeli nieodwiedzony to wywolujemy funkcje od nowa, z dlugoscia sciezki +1
                    count_paths(G,v, t, V, path_count,path+1) 
      
        V[u].visited = False 
        # po sprawdzeniu kazdej sciezki z wierzcholka nalezy zmienic na nieodwiedzony
        #pozwoli to sprawdzic inne sciezki z danym wierzcholkiem z innych wczesniejszych wierzcholkow

        
def count_shortest_paths(G, u, t, path_count):
    #utworzenie listy wierzcholkow
    V = []
    for i in range(len(G)):
        v = Vertex()
        v.id = i
        V.append(v)
    path = 0
    count_paths(G, u, t, V, path_count,path)
    #zwracamy liczbe sciezek o najkrotszej drodze
    return minimal(path_count)
    
    
path_count = []
G = [[False, True, True, False],
[False, False, True, True ],
[False, False, False, True ],
[False, False, False, False]]
print(count_shortest_paths( G, 0, 3,path_count ))