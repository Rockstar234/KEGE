def f(x,y,a,z):
    return (48!=y+2*x+z) or (a<x) or (a<y) or (a<z)

for a in range (0,1000):
    if all (f(x,y,a,z) == 1 for x in range (0,100) for y in range (0,100) for z in range (0,100)):
        print (a)
