def f(n,k):
    if n == k:
        return 1
    elif (n > k) or (n == 29):
        return 0
    else:
        return f(n+1, k) + f(n*2, k) + f(n*3, k)
print(f(2,13) * f(13,44))