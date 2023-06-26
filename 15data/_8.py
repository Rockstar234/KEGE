def f(x,a):
    return (((x % a != 0) and (x % 180 == 0)) <= (x % 130 == 0)) and (a < 100)

for a in range(1,1000):
    if all(f(x,a) == 1 for x in range(1,10000)):
           print(a)