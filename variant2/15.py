def f(x,y,a):
    return (3*x + 4*y != 70) or (a > x) or (a > y)

for a in range(1,1000):
    if all(f(x,y,a) == 1 for x in range(1,100) for y in range(1,100)):
           print(a)
           break
