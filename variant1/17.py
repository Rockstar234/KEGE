f = [int(x) for x in open('17.txt')]
s = []
for i in range(len(f)-2):
    sort = sorted([f[i], f[i+1], f[i+2]])
    if sort[2]**2 < (sort[1]**2 + sort[0]**2):
        s.append(f[i]+f[i+1]+f[i+2])
print(len(s), max(s))