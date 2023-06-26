f = [int(x) for x in open('17-3.txt')]
s=[]
for i in range(len(f)-2):
    if (f[i] * f[i+1] * f[i+2]) % 7 == 0 and abs(f[i] + f[i+1] + f[i+2]) % 10 == 5:
        s.append(f[i] + f[i+1] + f[i+2])
print(len(s), max(s))
