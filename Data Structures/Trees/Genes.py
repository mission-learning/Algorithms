class Node:
    def __init__(self,parent = None):
        self.A = None
        self.G = None
        self.C = None
        self.T = None
        self.parent = parent
        self.flag = 0
        
        
a = ["G","A","C"]
        
def insert(a,root = None):
    if root == None:
        root = Node()
        
    for letter in a:
        if letter is "A":
            if root.A == None:
                root.A = Node() 
            root = root.A
            
        elif letter is "C":
            if root.C == None:
                root.C = Node()
            root = root.C
            
        elif letter is "T":
            if root.T == None:
                root.T = Node()
            root = root.T
            
        elif letter is "G":
            if root.G == None:
                root.G = Node()
                
            root = root.G    
        
        if letter == a[len(a)-1]:
                if root.flag == True:
                    return 0
                else:
                    root.flag = True
    return 1

def check(A, root):
    for word in A:
        if(insert(word,root)==0):
            print("NO")
            return 
    print("Yes")
    return

A = [["A","G","C"],["A","G","C"],["G","G","C"],["A","A","C"],["A","G"]]
root = Node()
check(A,root)




           
                
    
    
    