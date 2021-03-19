#dynamiczne drzewa
#W lesie znajduje się n drzew stojących w jednej linii. Każde drzewo posiada określoną wartość, która
#należy traktować jako zysk po jego wycięciu. Nie możemy wyciąć więcej niż dwóch drzew pod rząd.
#Proszę zaimplementować funkcję pozwalającą określić które drzewa należy wyciąć, aby sumaryczny zysk
#był jak największy.


values = [3,4,8,1,10,1,100,200,10,5,10000]

#pomysl
#tworzymy tablice dynamiczna 
#element tablicy: tab[i][0] - oznacza ze wycinamy drzewo i, zakladajac brak wyciecia poprzedniego drzewa
#tab[i][1] - wciaz wycinamy i drzewo, ale z wycieciem drzewa i-1
#stad w wersji z 0 patrzymy na komorke i-2 (dowolnie wczesniej wyciete drzewo)
#a w wersji z 1 patrzymy na komorke i-1 gdzie poprzednie drzewo nie bylo wyciete, a wiec z 0


def dynamotree(values):
    tab = [[0 for i in range (2)] for i in range (len(values))]

    #drugi rzad stanowi o 1 - wycieciu drzewa wczesniej, 0 nie wycieciu drzewa i-1
    tab[0][0] = values[0]
    tab[0][1] = values[0]
    tab[1][1] = max(tab[0][0],tab[0][1]) + values[1]
    tab[1][0] = values[1]
    

    
    for i in range (2,len(values)):
        tab[i][1] = tab[i-1][0] + values[i]
        
        tab[i][0] = max(tab[i-2][0], tab[i-2][1]) + values[i]
       
        
    max_val = 0
    
    for i in range (len(values)-2,len(values)):
        for j in range(2):
            if max_val < tab[i][j]:
                x = i
                y = j
                max_val = tab[i][j]
    
    result = []
    
    while x > 0:
        
        result.insert(0,x)
        if y == 0:
            x = x-2
            if tab[x][0] == tab[x+2][0] - values[x+2]:
                y = 0
            else:
                y = 1
        else:
            x = x-1
            y = 0
                
    print(result)
        
    
    
dynamotree(values)