a = int('34', 8)
for x in range(1,1000):
    if a % x == 0 and (a//x) % x == 2:
        print(x)