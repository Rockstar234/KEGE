def f(x,a):
    return (((x&56!=0) <= (x&18!=0)) or (x&a!=0)) <= ((x&18==0) and (x&a==0) and (x&43!=0))

for a in range (10,51):
    if all (f(x,a) == 0 for x in range (0,1000)):
        print (a)
