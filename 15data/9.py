def f(x,a):
    return (((x % 36 == 0) and (x % 42 == 0)) <= (x % a == 0)) and (a * (a-25) < 25 * (a + 200))

for a in range(1,1000):
    if all(f(x,a) == 1 for x in range(1,10000)):
           print(a)