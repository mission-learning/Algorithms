class Node:
    def __init__(self,key,parent = None):
        self.rChild = None
        self.lChild = None
        self.parent = parent
        self.key = key
        self.bst = False
        
def insert(root, number):
    if root is None:
            root = Node(number)
    else:
            if root.key < number:
                if root.rChild == None:
                    root.rChild = Node(number,root)
                else:
                    insert(root.rChild,number)
            else:
                if root.lChild == None:
                    root.lChild = Node(number,root)
                else:
                    insert(root.lChild,number)
    return

def succ(node):
    n = node
    if n.rChild !=None:
        return min_tree(n.rChild)
    else:
        p = n.parent
        while (p != None):
            if n != p.rChild:
                break
            n = p
            p = p.parent
    return p

def deletion(root, key):
    n = if_inside(root,key)
    if n==None:
        return
    
    if n.lChild == None and n.rChild == None:
        n = n.parent
        if n.key>key:
            n.lChild = None
        else:
            n.rChild = None
    elif n.lChild != None and n.rChild == None:
        n = n.lChild
        
    elif n.rChild != None and n.lChild == None:
        n = n.rChild
        
    else:
        p = predec(n)
        tmp = p.key
        deletion(root, (predec(n).key))
        n.key = tmp
   

#korzystam z funkcji rekurencyjnej
#wykorzystuje postordertraversal
#zapisuje dane z lewego, prawego poddrzewa i porownuje z wartoscia maksymalna i rootem
#przekazuje dalej czy jest bst, liczba nodow w poddrzewie,maksymalne poddrzewo dotad widziane
        

def largest_bst(root,maxa):
    if root == None:
        return 0,True,maxa
    
    if root.lChild == None and root.rChild == None:
        root.bst = True
        return 1,True, max(maxa,1)

    left,left_bst,maxaleft = largest_bst(root.lChild,maxa)
    right,right_bst,maxaright = largest_bst(root.rChild,maxa)
    # zapis danych 
   
    if root.lChild == None: #jezeli nie ma dziecka to daje maksymalna/minimalna wartosc
        left_key = -1000
    else:
        left_key = root.lChild.key
       
    if root.rChild == None:
        right_key = 1000
    else:
        right_key= root.rChild.key
        
        
   
    if (left_bst and right_bst) and (left_key < root.key < right_key):
        
        return  left+right+1,True, max(maxa,left+right+1) #jesli korzen jest korzeniem drzewa bst
    else:
        
        return  0,False, max(left,right) #jesli nie jest zwracam wielkosc podrzewa wiekszego

     
         

root = Node(4)
root.rChild = Node(0,root)
root.lChild = Node(2,root)
root.lChild.lChild = Node(1,root)



print(largest_bst(root,0))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
