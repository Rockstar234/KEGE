f = [int(x) for x in open('17-1.txt')]
sr=sum(f)/len(f)
s=[]
for i in range(len(f)-2):
    if (f[i] < sr or f[i+1] < sr or f[i+2] < sr) and ((abs(f[i]) % 10 == 4 and abs(f[i+1]) % 10 == 4) or (abs(f[i+1]) % 10 == 4 and abs(f[i+2]) % 10 == 4) or (abs(f[i]) % 10 == 4 and abs(f[i+2]) % 10 == 4) or (abs(f[i]) % 10 == 4 and abs(f[i+1]) % 10 == 4 and abs(f[i+2]) % 10 == 4)):
        s.append(f[i]+f[i+1]+f[i+2])
print(len(s), max(s))