class Node:
    def __init__(self):
        self.next = None
        self.val = None

def printList( p ):
    while( p!=None ):
        print(p.val)
        p = p.next

    print()





def reverse( L ):
    if L.next == None :
        return L
    T = L.next
    H = reverse( T )
    T.next = L
    L.next = None
    return H

first = None
for i in range(6):
    p = Node()
    p.val = i*i
    p.next = first
    first = p
printList( first )
last = reverse( first )
printList( last )
