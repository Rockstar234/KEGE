def f(x,a):
    return (x & a !=0) <= ((x & 20 == 0) <= (x & 5 !=0))

for a in range(1,1000):
    if all(f(x,a) == 1 for x in range(1,10000)):
           print(a)

