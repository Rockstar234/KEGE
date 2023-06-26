def f(x,y,a):
    return (x>40) or (5*y-3*x>150) or (a>=(x-20)**2+(y-20)**2)

for a in range (1,10000):
    if all (f(x,y,a) == 1 for x in range (1,100) for y in range (1,100)):
        print (a)
        break
