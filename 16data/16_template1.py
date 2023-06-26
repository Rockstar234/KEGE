def f(n):
    c=1
#    print('*')
    if n>=1:
#        print('*')
        c=c+1+f(n-1)+f(n-2)+f(n-3)
    return c
print(f(22))