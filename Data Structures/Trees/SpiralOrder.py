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

def SpiralOrder(root):
    if root == None:
        return
    
    stack1 = []
    stack2 = []
    
    if root.lChild != None:
        stack1.append(root.lChild)
    if root.rChild != None:
        stack1.append(root.rChild)
        
    current = root
    print(current.key," ")
    
    while(len(stack1) or len(stack2)):
        
        while(len(stack1)):
            current = stack1.pop(-1)
            if current.rChild != None:
                stack2.append(current.rChild)
            if current.lChild != None:
                stack2.append(current.lChild)
            print(current.key," ")
                
        while(len(stack2)):
            current = stack2.pop(-1)
            if current.lChild != None:
                stack1.append(current.lChild)
            if current.rChild != None:
                stack1.append(current.rChild)
            print(current.key," ")
    
            
root = Node(15)
insert(root,10)
insert(root,20)
insert(root,8)
insert(root,12)
insert(root,7)
insert(root,9)
insert(root,11)
insert(root,13)
insert(root,18)
insert(root,17)
insert(root,19)
insert(root,22)
insert(root,21)
insert(root,24)

SpiralOrder(root)                               
            
            
            
                                 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    