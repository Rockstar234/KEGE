def f(x,a):
    return ((x & 29 == 0) or ((x & 11 == 0) <= (x & a != 0)))

for a in range(0,1000):
    if all(f(x,a) == 1 for x in range(15,31)):
        print(a)
        break