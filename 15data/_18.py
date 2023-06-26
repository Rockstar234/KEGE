def f(x,a):
    return (x&a==0) or ((x&69==4) <= (x&118==6))

for a in range (1,100):
    if all (f(x,a) == 1 for x in range (1,1000)):
        print (a)
