def f(x,y,a):
    return ((y>=-4*x+12) and (y>=4*x-12))==(y>=a*abs(x-3))

for a in range (1,1000):
    if all (f(x,y,a) == 1 for x in range (1,100) for y in range (1,100)):
                print (a)
