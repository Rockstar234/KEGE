f = [int(x) for x in open('17-342.txt')]
s=[]
ma=-1000000000
mi=1000000000 # кратное 37
for i in range(len(f)):
    if f[i] % 73 == 0:
        ma=max(ma, f[i])
for i in range(len(f)):
    if f[i] % 37 == 0:
        mi=min(mi, f[i])
print(ma, mi)
for i in range(len(f)-1):
    if ((ma < f[i] < mi) and (not(ma < f[i+1] < mi))) or ((ma < f[i+1] < mi) and (not(ma < f[i] < mi))):
        s.append(f[i] + f[i+1])
print(len(s), min(s))
