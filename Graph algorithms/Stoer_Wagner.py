#from dimacs import loadDirectedWeightedGraph
#from sys import argv
from queue import PriorityQueue


#(V,L) = loadDirectedWeightedGraph("graphs/flow/clique5")


V = 8
L = [[1,5,3],[1,2,2],[2,5,2],[2,6,2],[5,6,3],
     [2,3,3],[6,7,1],[3,4,4],[3,7,2],[7,4,2],[7,8,3],[8,4,2]]

#utworzenie list sasiedztwa na podstawie V i L

class Node:
  def __init__(self,i):
    self.edges = {}    # słownik  mapujący wierzchołki do których są krawędzie na ich wagi
    self.active = True
    self.packageOFVerticles = {i} #do przechowywania wierzcholkow z nim mergowanych

  def addEdge( self, to, weight):
    self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
                                                    # o zadanej wadze; a jeśli taka krawędź
                                                    # istnieje, to dodaj do niej wage
  def delEdge( self, to ):
    del self.edges[to]                              # usuń krawędź do zadanego wierzchołka
    
  def printNode(self):
      print(self.active, self.edges,)
      
def printGraph(G):
    for v in G:
        v.printNode()


def mergeVertices( G, x, y ):
    
    for edge in G[y].edges:
        
        if edge != x:
            G[x].addEdge(edge,G[y].edges[edge])
            G[edge].addEdge(x, G[y].edges[edge])
            
        G[edge].delEdge(y)
        
    G[y].edges = {}
    
    G[y].active = False
    #dezaktywujemy wierzcholek i dodajemy do zbioru wierzcholkow zmergowanych
    G[x].packageOFVerticles.add(y)
    
    
    
def getSum(G,i,S):
    suma = 0
    for edge in G[i].edges: 
        if edge in S:
            suma += G[i].edges[edge]
    return suma
    
    
def minimumCutPhase( G,size ):

  a = 1 # może to zawsze być wierzchołek numer 1 (lub 0 po przenumerowaniu)
  S = {a}
  order = [a] #do zapamietywania kolejnosci dodawania
  Q = PriorityQueue() 
  
  #tablica z sumami
  sums = []
  for i in range (len(G)):
      sums.append(getSum(G,i,S))
      Q.put((-sums[i],i))
   
  while len(S) < size:
      (suma, v) = Q.get()
      
      if v not in S:
          for edge in G[v].edges:
              sums[edge] += G[v].edges[edge]
              Q.put((-sums[edge],edge))
              maxSum = sums[edge]
              S.add(v)
          order.append(v)
          
  s = order[-1]
  potentialResult = sums[s]
  t = order[-2]
  
  # tworzone przecięcie jest postaci S = {s}, T = V - {s}

  minimumCut =  G[s].packageOFVerticles.copy()
  mergeVertices(G,s,t)
  
  printGraph(G)
  print("WYNIK POTENCJALNY:  ",potentialResult, minimumCut)
  print()

  return potentialResult,minimumCut


def Stoer_Wagner(L,V):
    #utworzenie listy sasiedztwa
    G = [ Node(i) for i in range(V+1) ]
    
    sizeOfGraph = V #no bo 0 wypada
    
    for (x,y,c) in L:
        G[x].addEdge(y,c)
        G[y].addEdge(x,c)
        
    printGraph(G)
        
    minimumResult = float('inf')
    minimumCut = {}
    
    while sizeOfGraph > 1:
        
        result,minCut = minimumCutPhase(G,sizeOfGraph)
        
        if result < minimumResult:
            minimumResult = result
            minimumCut = minCut
            
        sizeOfGraph -=1
        
    print(minimumResult, minimumCut)
        
    
Stoer_Wagner(L,V)   
    
    

    



  



  


    
                
        
            
    
        
        
        
        
        
        
        
    
