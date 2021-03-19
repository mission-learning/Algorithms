#rod cutting dynamic programming

rod = 4

price = [1, 5, 8, 9, 10, 17, 17, 20]

def rodCut(rod, price):
    
    
    tab = [[0 for i in range (rod+1)] for j in range (len(price)+1)]
    
    for i in range (1, rod + 1):
        tab[1][i] = i * price[0]
        #dzielac na kawalki dlugosci 1[pierwsza wspolrzedna] maksymalny profit dla dlugosci i roda 
        
        
    for i in range (1,len(price)+1):
        for j in range (1, rod + 1):
            
            if j - i >= 0:
                #jesli dlugosc roda jest wieksza niz kawalek ktory tniemy
                
                tab[i][j] = max(tab[i-1][j], price[i-1] + tab[i][j-i])
                #maksimum z wartosci uzyskanej dla roda j dlugosci bez i tego kawalka
                #oraz z wartosci roda, gdzie ucinamy i kawalek dodajac jego cene, ale dodajemy rod dla j-i dlugosci
                
            else:
                tab[i][j] = tab[i-1][j]
                #jezeli nie mozemy uciac juz kawalka i, bo rod jest za krotki, przepisujemy wartosc dla mniejszej liczby i
            
    print (tab[len(price)][rod])
    
    
    

    
rodCut(rod,price)