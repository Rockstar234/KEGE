f = [int(x) for x in open('17.txt')]
s=[]
for i in range(len(f)- 1):
    for j in range(i + 1, len(f)):
        if (f[i] + f[j]) % 120 == 0:
            s.append(f[i] + f[j])
print(len(s), max(s))