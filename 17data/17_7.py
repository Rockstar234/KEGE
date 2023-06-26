f = [int(x) for x in open('17-7.txt')]
s=[]
for i in range(len(f)):
    if f[i] % 8 == 7 and f[i] // 8 % 8 != 2:
        s.append(f[i])
print(len(s), max(s))