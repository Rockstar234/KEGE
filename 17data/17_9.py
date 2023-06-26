f = [int(x) for x in open('17-4.txt')]
s=[]
for i in range(len(f)):
    if (f[i] % 31 == 0 or f[i] % 47 == 0 or f[i] % 53 == 0) and (f[i] % 3 == f[i] % 5):
        s.append(f[i])
print(len(s), min(s))