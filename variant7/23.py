def f(n,k):
    if n == k:
        return 1
    elif (n < k) or (n == 8):
        return 0
    else:
        return f(n-2,k) + f(n//2,k)
print(f(70,22) * f(22,5))