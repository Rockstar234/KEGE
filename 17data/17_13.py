f = [int(x) for x in open('17-199.txt')]
s = []
for i in range(len(f)-2):
    if (f[i+1] % 2 == 0 and 10 <= f[i+1] <= 99) and not(f[i] % 2 == 0 and 10 <= f[i] <= 99) and not(f[i+2] % 2 == 0 and 10 <= f[i+2] <= 99):
        s.append(f[i]+f[i+1]+f[i+2])
print(len(s), max(s))