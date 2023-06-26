from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)-2*g(n-1)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)+g(n-1)+n
y = g(36)
print(sum(int(w) for w in str(y)))