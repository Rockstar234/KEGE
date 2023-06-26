f = [int(x) for x in open('17.txt')]
s = []
for i in range(len(f)-1):
    for j in range(i + 1, len(f)):
        raz = f[i] - f[j]
        if (raz % 36 == 0) and ((f[i] % 13 == 0) or f[j] % 13 == 0):
            s.append(f[i]-f[j])
print(len(s), max(s))