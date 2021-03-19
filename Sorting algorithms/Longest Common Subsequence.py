def LCSlength(x,y,lx,ly):
    if lx == 0 and ly == 0:
        return 0
    if (ly == 0) or (lx == 0):
        return 0
    if x[lx-1] == y[ly-1]:
        return LCSlength(x, y,lx-1,ly-1) + 1
    return max(LCSlength(x,y,lx,ly-1),LCSlength(x,y,lx-1,ly))


x = 'domikochatomi'
y = 'tomikochadomi'

print(LCSlength(x,y,len(x),len(y)))
