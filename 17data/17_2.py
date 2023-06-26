f = [int(x) for x in open('17-4.txt')]
s=[]
for i in range(len(f)):
    if (f[i] % 10 == 5 or f[i] % 10 == 7) and f[i] % 9 != 0 and f[i] % 11 != 0:
        s.append(f[i])
print(len(s), (min(s) + max(s)))