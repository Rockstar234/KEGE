def f(x,a):
    return ((a % 9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0))))

k=0
for a in range(1,1000):
    if all(f(x,a) == 1 for x in range(1,10000)):
           k=k+1
print(k)
           