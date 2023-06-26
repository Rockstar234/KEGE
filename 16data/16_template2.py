def f(n):
    c=0
    c=c+2*n
#    print(2*n)
    if n>1:
#        print(n-5)
        c=c+n-5+f(n-1)+f(n-2)
    return c
for n in range(1,1000):
    if f(n)>500000:
        print(n, f(n))
        break
