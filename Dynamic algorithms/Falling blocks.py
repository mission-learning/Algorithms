#Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai
#i ciągnie się
#do pozycji bi
#. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję
#tower(A), która wybiera możliwie najdłuższy podciąg klocków taki, że spadając tworzą wieżę i
#żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków. Do funkcji przekazujemy
#tablicę A zawierającą pozycje klocków ai
#,bi
#. Funkcja powinna zwrócić maksymalną wysokość wieży
#jaką można uzyskać w klocków w tablicy A.
#Przykład Dla tablicy A = [(1,4),(0,5),(1,5),(2,6),(2,4)] wynikiem jest 3, natomiast dla
#tablicy A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)] wynikiem jest 2.


A = [(1,4),(0,5),(1,5),(2,6),(2,4)]


def bigger_tower(a,b):
    (a1,a2) = a
    (b1,b2) = b
    
    if b1 >= a1 and b2 <= a2:
        return True
    else:
        return False
    
  
def least(a,b):
    
    (a1,a2) = a
    (b1,b2) = b
    
    a_res = a1
    b_res = a2
    
    if a1 < b1:
        a_res = b1
        
    if b2 < a2:
        b_res = b2
        
    return (a_res,b_res)
        

def fun(A):
    
    tab = [[1 for i in range (len(A))] for j in range (2)]
    
    for i in range (len(A)):
        tab[1][i] = A[i]
        
        
    result = 1
        
        
    for i in range (1,len(A)):
        for j in range (0,i):
            
            if bigger_tower(tab[1][j],A[i]):
                
                if tab[0][i] < tab[0][j]+1:
                    
                    tab[0][i] = tab[0][j]+1
                    tab[1][i] = least(A[i],tab[1][j])
                    
                    if result < tab[0][i]:
                        result = tab[0][i]
                    
    return result
                    

print(fun(A))