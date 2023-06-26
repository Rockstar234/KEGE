f = [int(x) for x in open('17-4.txt')]
s = []
for i in range(len(f)):
    if f[i] % 16 == 11 and f[i] % 7 == 0 and f[i] % 6 != 0 \
        and f[i] % 13 != 0 and f[i] % 19 != 0:
        s.append(f[i])
print(sum(s), len(s))