#from functools import *

#@lru_cache(None)
def f(n):
    if n==0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n//2)
    if n % 2 != 0:
        return 1 + f(n-1)
k=0
for i in range(1,1001):
    if f(i)==3:
        k+=1
print(k)