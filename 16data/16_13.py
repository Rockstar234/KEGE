def f(n):
    c=0
#    print('*')
    c += 1
    if n>=1:
#        print('*')
        c=c+1+f(n-1)+f(n//3)+1
#        print('*')
    return c
print(f(280))
