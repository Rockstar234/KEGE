f = [int(x) for x in open('17-1.txt')]
s = []
sr=sum(f)/len(f)
for i in range(len(f)-2):
    if (f[i] > sr and f[i+1] > sr) or (f[i+1] > sr and f[i+2] > sr) or (f[i] > sr and f[i+2] > sr) or (f[i+2] > sr and f[i] > sr and f[i+1] > sr):
        s.append(f[i]+f[i+1]+f[i+2])
print(len(s), max(s))