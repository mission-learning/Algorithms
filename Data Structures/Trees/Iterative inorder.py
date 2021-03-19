#iterative inorder


def I_Inorder(root):
    if root == None :
        return
    
    stack = []
    
    while (true):
        if root != None:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
        root = stack.pop(len(stack)-1)
        print(root.key)
        root = root.right
        