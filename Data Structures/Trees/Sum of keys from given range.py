class Node:
    def __init__(self,key,parent,rightsum,leftsum):
        self.rChild = None
        self.lChild = None
        self.parent = parent
        self.key = key
        self.leftsum = leftsum
        self.rightsum = rightsum
        
def insert(root, number,rightsum,leftsum):
   
            if root.key < number:
                if root.rChild == None:
                    root.rChild = Node(number,root,rightsum,leftsum)
                else:
                    insert(root.rChild,number,rightsum,leftsum)
            else:
                if root.lChild == None:
                    root.lChild = Node(number,root,rightsum,leftsum)
                else:
                    insert(root.lChild,number,rightsum,leftsum)
            return
        
        
def sum_xy(root,x,y):
    
    n = root
    
    while True: #szukanie wierzcholka znajdujacego sie w srodku przedzialu
    
        if x < n.key and y < n.key:        
            n = n.lChild
        elif x > n.key and y >n.key:
            n = n.rChild
        else:
            break
        
    sum_left = 0
    sum_right = 0
    
    n_x = n.lChild
    n_y = n.rChild
    
    while(n_x != None):     #suma lewej strony
        if n_x.key >= x:
            sum_left+=n_x.rightsum + n_x.key #jezeli klucz znajduje sie w przedziale to jego prawe poddrzewo tez
            n_x = n_x.lChild
        else:
            n_x = n_x.rChild
            
    while(n_y != None): #suma prawej strony
        if n_y.key <= y:
            sum_right += n_y.leftsum + n_y.key
            n_y= n_y.rChild
        else:
            n_y = n_y.lChild
    
    return sum_left + sum_right + n.key 
        

root = Node(15,None,63,30)
insert(root,10,12,8)
insert(root,8,0,0)
insert(root,12,0,0)
insert(root,20,25,18)
insert(root,25,0,0)
insert(root,18,0,0)

print(sum_xy(root,18,25))



