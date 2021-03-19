class Node:
    def __init__(self,key,parent = None):
        self.rChild = None
        self.lChild = None
        self.parent = parent
        self.key = key
        self.leftUnder = 0
        self.rightUnder = 0

    
def insert(root, number):
    if root is None:
            root = Node(number)
    else:
            if root.key < number:
                root.rightUnder+=1
                if root.rChild == None:
                    root.rChild = Node(number,root)
                else:
                    insert(root.rChild,number)
            else:
                root.leftUnder+=1
                if root.lChild == None:
                    root.lChild = Node(number,root)
                else:
                    insert(root.lChild,number)
    return

def inorder(root):
    if root: 
        inorder(root.lChild) 
        print(root.key) 
        inorder(root.rChild) 
        
def if_inside(root,key):
    if root.key == key:
       
        return root
    else:
        if root.key > key:
            if root.lChild == None:
               
                return None
            else:
                return if_inside(root.lChild,key)
        else:
            if root.rChild == None:
               
                return None
            else:
                return if_inside(root.rChild,key)
                
def min_tree(root):
    tmp = root
    while(tmp.lChild!=None):
        tmp = tmp.lChild
    return tmp

def max_tree(root):
    tmp = root
    while(tmp.rChild!=None):
        tmp = tmp.rChild
    return tmp

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

def predec(node):
    n = node
    if n.lChild != None:
        return max_tree(n.lChild)
    else:
        p = n.parent
        while (p != None):
            if n == p.rChild:
                break
            n = p
            p = p.parent
    return p



def treesum(root,summ = 0):
    if root: 
        summ+=root.key+ treesum(root.rChild,summ)+treesum(root.lChild,summ) 
        return summ
    else:
        return 0

def sumconst(n):
    
    while (n.lChild  != None or n.rChild != None):       
        while (n.lChild != None):       
            n = n.lChild
        
        if (n.rChild != None):
            n = n.rChild
    sum = 0
    pre = None
    
    while n!= None:
        if pre != n.rChild:
            if (n.rChild != None):
                n = n.rChild
                while (n.lChild != None or n.rChild != None):
                    while n.lChild != None:
                        n = n.lChild
                    if n.rChild != None:
                        n = n.rChild
            else:
                sum += n.key
                pre = n
                n = n.parent
        else:
            sum += n.key
            pre = n
            n = n.parent
    return sum


def deletion(root, key):
    n = if_inside(root,key)
    x = n
    if n==None:
        return
    
    if n.lChild == None and n.rChild == None:
        n = n.parent
        if n.key>key:
            n.lChild = None
            n.leftUnder -=1
        else:
            n.rChild = None
            n.rightUnder-=1
            
    elif n.lChild != None and n.rChild == None:
        n.lChild.parent = n.parent
        child = n.lChild
        n = n.parent       
        if n.key>key:
            n.lChild = child
            n.leftUnder-=1
        else:
            n.rChild = child
            n.rightUnder-=1
        
    elif n.rChild != None and n.lChild == None:
        n.rChild.parent = n.parent
        child = n.rChild
        n = n.parent       
        if n.key>key:
            n.lChild = child
            n.leftUnder-=1
        else:
            n.rChild = child
            n.rightUnder-=1
        
    else:
        p = n.lChild
        while(p.rChild!=None):
            p = p.rChild
            
            
        tmp = p.key
        deletion(root, p.key)
        n.key = tmp

    x = x.parent
    
    if x!= None:
        while(x.parent != None):
            x = x.parent
            if x.key > key:
                x.leftUnder-=1
            else:
                x.rightUnder-=1
            key = x.key
        
    
        
def isBST(node, minKey, maxKey):

	if node is None:
		return True

	if node.key < minKey or node.key > maxKey:
		return False

	return isBST(node.lChild, minKey, node.key) and isBST(node.rChild, node.key, maxKey)


def LowestAncestor(root,x,y):
    if root == None:
        return None
    if root.key > max(x.key,y.key):
        return LowestAncestor(root.lChild,x,y)
    elif root.key < min(x.key,y.key):
        return LowestAncestor(root.rChild,x,y)
    
    return root

def kthSmallest(root,i,k):          #recursion
    if root is None:
        return None,i
    
    left,i = kthSmallest(root.lChild, i,k)
    
    if left != None:
        return left,i
    
    i+=1
    
    if i == k:
        return root,i
    
    return kthSmallest(root.rChild,i,k)

def findFloorCeil(root, floor, ceil, key):

    if root is None:
        return floor, ceil

    if root.key == key:
        return root, root

    elif key < root.key:
        return findFloorCeil(root.lChild, floor, root, key)

    else:
        return findFloorCeil(root.rChild, root, ceil, key)    
    
def inorderunder(root): 
    if root: 
        inorderunder(root.lChild) 
        print(root.leftUnder,root.key,root.rightUnder) 
        inorderunder(root.rChild) 
        
        
def kth_with_undertree(root,k):
    
    if k == root.leftUnder+1:
        return root
    elif k < root.leftUnder+1:
        return kth_with_undertree(root.lChild, k)
    elif k > root.leftUnder+1:
        return kth_with_undertree(root.rChild, k-root.leftUnder-1)


def which_am_i(root, key):
    
    indx =  1
    
    node = if_inside(root,key)
    if node == None:
        return 0
    if node.parent == None:
        return node.leftUnder + 1
    
    indx += node.leftUnder
    
    while node.parent != None:
        
        
        if node.key < node.parent.key:
            
            node = node.parent
            
        elif node.key > node.parent.key:
            
            node = node.parent
            indx += 1 + node.leftUnder
    
    return indx

def inorder_list(root, A):
    if root: 
        inorder_list(root.lChild,A) 
        A.append(root.key) 
        inorder_list(root.rChild,A) 

def common_elements(root_1, root_2):
    
    list_1 = []
    list_2 = []
    
    inorder_list(root_1, list_1)
    inorder_list(root_2, list_2)
    
    print(list_1)
    print(list_2)
    
    i, j = 0,0
    result = 0
    
    while (i != len(list_1) and j != len(list_2)):
        
        if list_1[i] == list_2[j]:
            result += 1
            i += 1
            j += 1
        elif list_1[i] < list_2[j]:
            i += 1
        elif list_1[i] > list_2[j]:
            j += 1
            
    return result 


def countInterval(root,x,y):
    n = root
    
    while True: #szukanie wierzcholka znajdujacego sie w srodku przedzialu
    
        if x < n.key and y < n.key:        
            n = n.lChild
        elif x > n.key and y >n.key:
            n = n.rChild
        else:
            break
        
    left = 0
    right = 0
    
    n_x = n.lChild
    n_y = n.rChild
    
    while(n_x != None):     #suma lewej strony
        if n_x.key >= x:
            left+=n_x.rightUnder + 1 #jezeli klucz znajduje sie w przedziale to jego prawe poddrzewo tez
            n_x = n_x.lChild
        else:
            n_x = n_x.rChild
            
    while(n_y != None): #suma prawej strony
        if n_y.key <= y:
            right += n_y.leftUnder + 1
            n_y= n_y.rChild
        else:
            n_y = n_y.lChild
    
    return left + right + 1
        

def main():
    root = Node(15)
    insert(root,20)
    insert(root,10)
    insert(root,12)
    insert(root, 8)
    insert(root, 18)
    insert(root,25)
    
    
    print(countInterval(root,17,20))
    

    
main()




        
    