#Floyd_Warshall
#do wyznaczenia domkniecia przechodniego modyfikujemy algorytm floyda warshalla
#nie wyznaczamy najkrotszych sciezek, a jedynie sprawdzamy, czy istnieje sciezka miedzy danymi wierzcholkami
#stad wystarczy zamienic dotychczasowe operatory na operatory logiczne
#OR - wystarczy ze albo juz znalezlismy sciezke wczesniej, albo mozemy dojsc do danego wierzcholka 
#z aktualnie przetwarzanego(wyjetego z kolejki)

#AND -musi jednoczesnie istniec sciezka z i" do wierzcholka przetwarzanego (t) oraz krawedz z niego do wierzcholka sprawdzanego (t,j)


def tclosure(graph): 
    n = len(graph)
    S = graph
    for t in range(n):
        for i in range(n):
            for j in range(n): 
                S[i][j] = (S[i][j] or (S[i][t] and S[t][j]))
    return S



# policz domknięcie przechodnie G i je zwróc
G = [ [False, True , False],
[False, False, True ],
[False, False, False] ]
print( tclosure( G ) ) # wypisze
# [[False, True , True],
# [False, False, True],
# [False, False, False]]