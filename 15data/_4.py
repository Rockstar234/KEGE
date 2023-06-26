def f(x,y,a):
    return (2*y + x != 17) or ( a>7*x) and (a>3*y)

for a in range (1,1000):
    if all (f(x,y,a) == 1 for x in range (1,100) for y in range (1,100)):
        print (a)
        break