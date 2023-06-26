def f(x,y,a):
    return (y-x<a) or (7*x+4*y>350) or (3*y-2*x>45)

for a in range (1,1000):
    if all (f(x,y,a) == 1 for x in range (1,100) for y in range (1,100)):
        print(a)
        break