def f(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n//2) + 1
    if n >= 2 and n % 2 != 0:
        return f(3*n+1)+1
s=[]
for i in range(1,100001):
    if f(i)==16:
        s = [i] + s
print(len(s)) # 24

#k=0
#for i in range(1,100001):
#    if f(i)==16:
#        k += 1
#print(k)
