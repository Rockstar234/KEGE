def f(x,a):
    return ((x&56!=0) or (x&43!=0)) <= (x&a!=0)

for a in range (75,126):
    if all (f(x,a) == 1 for x in range (0,1000)):
        print (a)
