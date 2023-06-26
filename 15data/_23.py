def f(x,a,r):
    return (((x&54==0) or (x&45==0)) <= ( x&a==0)) or (x&r==0)

for r in range (10,51):
    if all (f(x,a,r) == 1 for x in range (1,100) for a in range (1,100)):
        print (r)
