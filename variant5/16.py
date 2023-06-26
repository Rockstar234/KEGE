from functools import *

@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n % 2 != 0 and n > 0:
        return f(n-1) + 1
    if n > 0 and n % 2 == 0:
        return f(n//2)
k=0
for n in range(100000000):
    f(n)
    if f(n)==2:
        k+=1
print(k)
