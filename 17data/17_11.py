f = [int(x) for x in open('17-243.txt')]
s=[]
maxc=max(x for x in f if x % 119 == 0)
for i in range(len(f)-1):
    if (f[i] > maxc or f[i+1] > maxc) and (f[i] % 100 == 21 or f[i+1] % 100 == 21):
        s.append(f[i]+f[i+1])
print(len(s), min(s))