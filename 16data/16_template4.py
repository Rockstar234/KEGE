from functools import *

@lru_cache(None)

def f(n):
    if n <= 5:
        return 2*n
    if n > 5 and n % 2 == 0:
        return f(n-2)+3*f(n//2)+n
    if n > 5 and n % 2 != 0:
        return f(n-1)+f(n-2)+f(n-3)
for n in range(0,1000):
    f(n)
print(f(999)+f(1000))
#def f(n):
#    if n <= 5:
#        return 2*n
#    if n > 5 and n % 2 == 0:
#        return f(n-2)+3*f(n//2)+n
#    if n > 5 and n % 2 != 0:
#        return f(n-1)+f(n-2)+f(n-3)
#print(f(99)+f(100))