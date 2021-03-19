#Do wyznaczenia sumy z danego przedziału można wykorzystać strukturę segment-tree, które
#stanowi modyfikacje drzewa przedzialowego

#utworzone drzewo w ponizszy sposob posiada wszystkie poziomy zapelnione poza ostatnim, co jest spowodowane
#dzieleniem dzieki funkcji getMid na polowy, a proces jest wykonywany dla kazdego poziomu

#drzewo posiada reprezentacje tablicowa, dzieki czemu dostanie sie do dzieci jest takie jak w kopcu, ktory byl omawiany na zajeciach
# lewe dziecko - 2*index+1, prawe dziecko 2*index+2

#liscie drzewa to elementy z tablicy, wyzsze wierzcholki drzewa stanowia przedzialy

#im wyzszy poziom tym wiecej przedzialow bazowych znajduje sie w danym wierzcholku

#kazdy przedzial jest reprezentowany dzieki temu przez maksymalnie 2 wierzcholki na danym poziomie, tak jak w drzewie przedzialowym
#sumowianie dla danego przedzialu polega na przejsciu wierzchokow,znalezenie sumy w jego lewym/i lub prawym poddrzewie w zależnosci gdzie dany przedzial sie miesci

#podczas aktualizacji wartosci na lisciu, konieczne jest odswiezenie rowniez wyzszych wartosci co zapewnia nam funkcja update




from math import  log2; 

def getMid(start, end) : 
    return start + (end - start) // 2;  
def getMidd(start, end) : 
    return (end - start) // 2;  

  

def getSum_interval(segment_tree, start, end, qstart, qend, cur) :  
  
    if (qstart <= start and qend >= end) : #jesli dany segment nalezy do przedzialu dodajemy go 
        return segment_tree[cur];  
  
    if (end < qstart or start > qend) :     #jesli nie nalezy
        return 0;  
  
    mid = getMid(start, end) #wyznaczenie srodka przedzialu
    
    #podzial i sumowanie lewej i prawej strony
    
    return getSum_interval(segment_tree, start, mid, qstart, qend, 2 * cur + 1) + getSum_interval(segment_tree, mid + 1, end, qstart, qend, 2 * cur + 2);  

def updateValue(segment_tree, start, end, index, diff, cur) :  
  
    if (index < start or index > end) : 
        return;  
  
    segment_tree[cur] = segment_tree[cur] + diff
      
    if (end != start) : 
      
        mid = getMid(start, end);  
        updateValue(segment_tree, start, mid, index, diff, 2 * cur + 1)
        updateValue(segment_tree, mid + 1, end, index, diff, 2 * cur + 2);  
  
def update(array, segment_tree, n, index, new_val) :  

    diff = new_val - array[index];  
  
    array[index] = new_val;  
  
    updateValue(segment_tree, 0, n - 1, index, diff, 0);  
   
def ceiling(x):
    return int(x+1)
  

def constructSegmentTree(array, start, end, segment_tree, cur) :  

    if (start == end) : 
      
        segment_tree[cur] = array[start];  
        return array[start];  
      
    mid = getMid(start, end);  
      
    segment_tree[cur] = constructSegmentTree(array, start, mid, segment_tree, cur * 2 + 1) + constructSegmentTree(array, mid + 1, end, segment_tree, cur * 2 + 2);  
      
    return segment_tree[cur];  
  
def constructST(array, n) :  
   
    x = ceiling(log2(n));  #ustalenie wysokosci drzewa, ma log2n poziomow, gdyz dzielac na polowy struktura przypomina pelne drzewo binarne
  
    max_size = 2 * int(2**x) - 1; #maksymalny rozmiar drzewa
    
    segment_tree = [0 for i in range (max_size)]

    constructSegmentTree(array, 0, n - 1, segment_tree, 0);  

    return segment_tree;  
   
### KLASA
class IntervalSums:
    def __init__(self, n):
        self.table = [0 for i in range(n)]
        self.segment_tree = constructST(self.table,n)
        
    def set( self, i, val, n ):
         update(self.table, self.segment_tree, n, i, val); 
        
    def interval( self, i, j ,n):
        print(getSum_interval(self.segment_tree,0,n-1,i,j,0))
        


IS = IntervalSums(4) # tworzy tablicę [0,0,0,0]
IS.set(0,10,4) # [10,0,0,0]
IS.set(2,-2,4) # [10,0,-2,0]
IS.set(3,1,4) # [10,0,-2,1]
IS.interval(0,3,4) # zwraca 10+0+(-2)+1 = 9
IS.interval(1,2,4) # zwraca 0-2 = -2

print(getMidd(3, 8) ) 
     