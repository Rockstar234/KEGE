def f(x,a):
    return ((a % 3 == 0) and ((220 % x == 0) <= ((a % x != 0) <= (550 % x != 0))))

for a in range(1,1001):
    if all(f(x,a) == 1 for x in range(1,10000)):
           print(a)
           