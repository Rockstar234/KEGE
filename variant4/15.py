def f(x,a):
    return (160 <= x <= 180) <= ((x % 35 == 0) <= (x % a == 0))

for a in range(1,10000):
    if all(f(x,a) == 1 for x in range(1,10000)):
        print(a)
