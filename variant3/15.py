def f(x,a):
    return ((x in a) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in a))

for a in range (-1000,1000):
    if all (f(x,a) == 1 for x in range (0,1000)):
        print(a)
