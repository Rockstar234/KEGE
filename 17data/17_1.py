f = [int(x) for x in open('17-4.txt')]
s=[]
for i in range(len(f)):
    if f[i] % 3 == 0 and f[i] % 7 != 0 and f[i] % 17 != 0 \
        and f[i] % 19 != 0 and f[i] % 27 != 0:
        s.append(f[i])
print(len(s), max(s))