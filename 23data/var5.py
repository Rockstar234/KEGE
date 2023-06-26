def f(n,k):
    if n == k:
        return 1
    elif n > k:
        return 0
    else:
        return f(n+1,k) + f(n+2,k) + f(n+6,k)
print(f(21,30))
