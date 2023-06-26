def f(x,a):
    return ((not(x in a)) <= (((17 <= x <= 46) and (22 <= x <= 57)) <= (x in a)))

for a in range(1,1000):
    if all(f(x,a) == 1 for x in range(1,1000)):
        print(a)