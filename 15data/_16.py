def f(x,a):
    return ((x&a!=0) <= (x&55==44)) or (x&112!=16)

for a in range (1,1000):
    if all (f(x,a) == 1 for x in range (0,1000)):
        print (a)
