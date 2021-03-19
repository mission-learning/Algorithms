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

def inorder(root):
    res = []
    if root:
        res += inorder(root.lChild)
        res.append(root.key)
        res += inorder(root.rChild)
    return res
        
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
    

def inorder_tree_maker(root,A,i):
    if root:
        i = inorder_tree_maker(root.lChild,A,i)
        root.key = A[i]
        i+=1
        i = inorder_tree_maker(root.rChild,A,i)
    return i

         
def main():
    root = Node(4)
    root.lChild = Node(5,root)
    root.rChild = Node(3,root)
    root.lChild.lChild = Node(1,root.lChild)
    root.lChild.rChild = Node(7,root.lChild)
    
    A = (inorder(root))
    A = sorted(A)
    
    inorder_tree_maker(root,A,0)
    
    print(inorder(root))
    
    
    
    
    
   
    
    
    

    
main()




        
    