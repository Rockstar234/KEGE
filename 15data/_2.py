def f(x,y,a):
    return (y-x>a) or (x+4*y>40) or (y-2*x<-35)

for a in range (-100,1000):
    if all (f(x,y,a) == 1 for x in range (1,100) for y in range (1,100)):
        print (a)
