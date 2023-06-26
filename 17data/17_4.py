f = [int(x) for x in open('17-5.txt')]
s = []
for i in range(len(f)-1):
    if abs(f[i]) % 10 == 7 or abs(f[i+1]) % 10 == 7:
        s.append(f[i]+f[i+1])
print(len(s), max(s))