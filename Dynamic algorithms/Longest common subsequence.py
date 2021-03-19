#najdluzszy wspolny podciag iteracyjnie

#idziemy od konca
#indeksy s1,s2 robia jako 0,0
#w 0,0 mamy wynik
#jezeli ostatnia litera sie zgadza to dodajemy 1 do poprzedniego wyniku
#jezeli sie nie zgadza patrzymy na napis bez literki w s1 lub s2 a wiec i+1/j+1

def LCS(s1,s2):
    
    tab = [[0 for i in range (len(s1)+1)] for j in range (len(s2)+1)]
    
    size1 = len(s1)
    size2 = len(s2)
    
        
    for i in range (size2-1,-1,-1):
        for j in range(size1-1,-1,-1):
            
            if s1[j] == s2[i]:
                
                tab[i][j] = 1 + tab[i+1][j+1]
            else:
                tab[i][j] = max(tab[i+1][j],tab[i][j+1])
                
    
    return tab[0][0]

s1 = "tomi"
s2 = "domii"

print(LCS(s1,s2))