from
def f(n):
    if n >= 11:
        return n
    if n < 11:
        return n**3 + f(n+2)
print(f(4)-f(10))