#Zbiór przedziałów {[a1, b1], ..., [an, bn]}, każdy przedział należy do [0, 1]. Opisać algorytm który
#sprawdzi czy jest możliwy taki wybór przedziałów, aby cały przedział [0, 1] zawierał się w
#wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.


#sortujemy po poczatku przedzialow
#przechodzimy liniowo po przedzialach
#utrzymujac koniec ostatniego przedzialu przechodzimy po tych zaczynajacych sie wczesniej niz ten koniec
#wybieramy z nich taki przedzial, co sie konczy najpozniej


A = [[1,2],[0,1],[4,7],[4,6],[6,9],[8,10],[9,10],[3,4],[0,3],[3,7],[7,10]]

A = sorted(A,key = lambda tup : tup[0])
print(A)

def min_intervals(A):
    
    result = []
    i = 0
    
    start = 0
    end = 0
    
    tmp_start = 0
    tmp_end = 0
    
    while i < len(A):
        
        tmp_end = A[i][1]
        tmp_start = A[i][0]
        flag = 1
        
        
        while A[i][0] <= end:
            
            if tmp_end < A[i][1] :
                
                tmp_end = A[i][1]
                tmp_start = A[i][0]
                
            i=i+1
            flag = 0
            if i == len(A):
                break
            
            
        if flag == 1:
            i=i+1
        
        result.append([tmp_start,tmp_end])
        end = tmp_end
        
        if end == 10:
            break
                      
    print(result)
    
    
min_intervals(A)

            
        
        
       
        
    
    