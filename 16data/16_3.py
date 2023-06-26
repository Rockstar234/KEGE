from functools import *

@lru_cache(None)
def f(n):
    if n < 4 or n % 2 != 0:
        return 1
    if n > 3 and n % 2 == 0:
        return f(n-1)+f(n-2)+f(n-3)
for n in range(0, 10000):
    f(n)
print(f(2008)-f(2006))