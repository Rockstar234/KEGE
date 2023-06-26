f = [int(x) for x in open('17-3.txt')]
s = []
for i in range(len(f)-1):
    y = abs(f[i] * f[i+1])
    if (f[i] + f[i+1]) % 3 == 0 and (f[i] + f[i+1]) % 6 != 0 and y % 10 == 8:
        s.append(f[i]+f[i+1])
print(len(s), max(s))