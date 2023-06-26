for x in range(3,1000):
    a = 1 * x**0 + 2 * x**1 + 1 * x**2 + 1
    b = 1 * 7**0 + 0 * 7**1 + 1 * 7**2
    if a == b:
        n = x
        break
s = []
while n > 0:
    s = [n % 3] + s
    n = n//3
print(s,x)
            
            
