def f(x,a):
    return (not(not(x in a)) and (22 <= x <= 72)) or (42 <= x <= 102)

for a in range(1,1001):
    if all(f(x,a) == 1 for x in range(1,10000)):
        print(a)