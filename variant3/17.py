f = [int(x) for x in open('17.txt')]
s=[]
for i in range(len(f)-1):
#    if (f[i] % 3 == 0 and f[i+1] % 3 !=0) or (f[i] % 3 != 0 and f[i+1] % 3 ==0) or (f[i] % 3 == 0 and f[i+1] % 3 ==0):
    if (f[i] % 3 == 0 or f[i+1] % 3 == 0):
        s.append(f[i]+f[i+1])
print(len(s), max(s))