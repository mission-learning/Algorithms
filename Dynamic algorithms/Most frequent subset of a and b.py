#Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
#ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
#mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
#ciąg składa się wyłącznie z liter a i b.
#Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
#powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
#algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.

class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
        self.count = 1
        

def h(key):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255
    
    return v % N

def insert(hash_tab, key):
    idx = h(key)
    for i in range(N):
        if hash_tab[idx].taken:
            idx = (idx + 1) % N
        else:
            break
    
    if not hash_tab[idx].taken:
        hash_tab[idx].key = key
        hash_tab[idx].taken = True


def find(hash_tab, key):
    idx = h(key)
    for i in range(N):
        if not hash_tab[idx].taken: return None
        if hash_tab[idx].key == key: return idx
        idx = (idx + 1) % N
    
    return None

N = 20
hash_tab = [Node() for i in range(N)]


#wykorzystuje hashowanie oraz funkcje rekurencyjna
#albo biore literke i hashuje slowo jesli osiagnelam liczbe liter zadana
#albo nie biore literki


def count(A,k,hasht,f,word,i):
    
    if len(A)-i + f < k:
        return
    if f > k:
        return
    if k == f:
        if find(hasht,word) == None:
            insert(hasht,word)
        else:
            hasht[find(hasht,word)].count+=1
        return
    if len(A) == i:
        return 0
   
    
    count(A,k,hasht,f,word,i+1)
    count(A,k,hasht,f+1,word+A[i],i+1)
    
count("babba",3,hash_tab,0,"",0)

for el in hash_tab:
    print(el.key,el.count)





















