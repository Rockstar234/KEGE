def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n//2)-1
    if n > 0 and n % 2 != 0:
        return 3 + f(n-1)
y = set()
for i in range(1,1000):
    y.add(f(i))
print(len(y))